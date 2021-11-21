import asyncclick as click

from app import config
from app.db_api.database import connect
from app.db_api.models import User
from app.loader import db
from loguru import logger


@click.command()
@click.option('-d', '--drop', is_flag=True, help='Delete the created table')
@click.option('-a', '--add-admins', is_flag=True, help="Add the admin_id's from environment variable")
async def cli(drop: bool = False, add_admins: bool = False):
    await connect()

    if drop:
        logger.warning('Dropping tables')
        await db.gino.drop_all()

    logger.info('Creating tables')
    await db.gino.create_all()

    if add_admins:
        logger.info('Adding administrators')
        for admin_id in config.ADMINS_ID:
            await User.create(id=int(admin_id), is_superuser=True)
            logger.debug(f'Administrator {admin_id} was added to the table')

    await db.pop_bind().close()


if __name__ == "__main__":
    cli(_anyio_backend='asyncio')
