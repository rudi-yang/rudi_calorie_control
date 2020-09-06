class SqlCollection():
    SQL_CREATE_TABLE_CALORIE_CONTROL = """
    create table if not exists calorie_control
    (
       id integer primary key  autoincrement,
       action text not null,
       cate text not null,
       detail text not null,
       ds int
    );"""

    SQL_INSERT_CALORIE_CONTROL = """
    insert into calorie_control(action, cate,  detail, ds)
                values ('{0}', '{1}', '{2}', '{3}');
    """

    SQL_DROP_TABLE_CALORIE_CONTROL = """
    drop table if exists calorie_control;
    """

    SQL_DROP_CALORIE_CONTROL_BY_ID = """
    delete from calorie_control where id='{0}';
    """
