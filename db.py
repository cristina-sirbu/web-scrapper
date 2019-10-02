import sqlite3


class DB:
    id = 0

    def __init__(self, name):
        try:
            self.sqlite_connection = sqlite3.connect('name')
            self.cursor = self.sqlite_connection.cursor()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    def run_query(self, query):
        self.cursor.execute(query)
        self.sqlite_connection.commit();
        return self.cursor.fetchall()

    def create_table(self, name):
        create_table_query = '''CREATE TABLE IF NOT EXISTS ''' + name + ''' (
                                                        id INTEGER PRIMARY KEY,
                                                        name TEXT NOT NULL,
                                                        price REAL NOT NULL,
                                                        category TEXT NOt NULL,
                                                        image_url text NOT NULL);'''
        self.run_query(create_table_query)

    def insert_into_table(self, table_name, item):
        insert_into_table_query = '''INSERT INTO `''' + table_name + '''`
                          ('id', 'name', 'price', 'category', 'image_url')  VALUES
                          ('''+str(self.id)+''',\''''+item.name+'''\',\''''+item.price+'''\',\''''+item.category+'''\',\''''+item.image_url+'''\');'''
        self.id += 1
        self.run_query(insert_into_table_query)

    def check_if_item_exists_in_table(self, table_name, item):
        select_item_query = '''
            SELECT count(*) FROM ''' + table_name + '''
            WHERE name == \'''' + item.name + '''\'
            AND price == \'''' + item.price + '''\'
            AND category == \'''' + item.category + '''\'
            AND image_url == \'''' + item.image_url + '''\''''
        if self.run_query(select_item_query)[0][0] > 0:
            return True
        else:
            return False

    def close_conn(self):
        self.cursor.close()
        self.sqlite_connection.close()
        print("The SQLite connection is closed")
