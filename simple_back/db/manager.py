import sqlalchemy


class DBConfig:
    def get(self):
        return dict(host=None,
                    port=None,
                    db=None,
                    user=None,
                    password=None)


class DBConfigPostgresLocal(DBConfig):
    def get(self):
        return dict(host='localhost',
                    port='5432',
                    db='testdb',
                    user='admin',
                    password='admin')


class DBConfigPostgresLocalDocker(DBConfig):
    def get(self):
        return dict(host='172.17.0.1',
                    port='5432',
                    db='testdb',
                    user='admin',
                    password='admin')


def get_sqlalchemy_postgres_db_engine(db, user, host, port, password, pool_size=50):
    """
    Get SQLalchemy engine using credentials.
    Input:
    db: database name
    user: Username
    host: Hostname of the database server
    port: Port number
    passwd: Password for the database
    """

    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    engine = sqlalchemy.create_engine(url, pool_size=pool_size)
    return engine


class SqlAlchemyPostgresDBEngine:
    def __init__(self, db_config: DBConfig):
        self.__db_config = db_config
        self.__engine = None

    def get_engine(self):
        if self.__engine:
            return self.__engine

        self.__engine = get_sqlalchemy_postgres_db_engine(**self.__db_config.get())
        return self.__engine

    def version(self):
        connection = self.get_engine().connect()
        result = connection.execute('SELECT version()')
        version = result.fetchone()
        connection.close()
        return version
