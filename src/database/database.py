
import psycopg2


def execute_query(query):
    try:
        conn = psycopg2.connect(
            "dbname=temperatures user=postgres password=password")
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_temperature_data(site_id, org_id, temperature, timestamp):
    # TODO: Overwrite existing row if we don't want historic data
    # TODO: Modify key for the table to account for multiple records
    #  from the same site
    query = f"""
    CREATE TABLE IF NOT EXISTS temperature_records (
        site_id VARCHAR(255) PRIMARY KEY,
        org_id VARCHAR(255),
        temperature REAL,
        timestamp INTEGER
    );
    INSERT INTO temperature_records
    VALUES ('{site_id}', '{org_id}', {temperature}, {timestamp})
    """
    execute_query(query)


def get_last_temperature_with_site_id(site_id: str):
    # TODO: Query is failing.
    query = f"""
    SELECT a.site_id, a.temperature, a.timestamp
    FROM temperature_records a
    INNER JOIN (
        SELECT site_id, MAX(timestamp) timestamp
        FROM temperature_records
        GROUP BY site_id
    ) b ON a.id = b.id AND a.rev = b.rev
    WHERE site_id='{site_id}'
    """
    execute_query(query)


def is_too_hot(site_id: str):
    pass


if __name__ == '__main__':
    insert_temperature_data('abc123', 'alphacorp', 27.3, '1658739178')
    get_last_temperature_with_site_id('abc123')
