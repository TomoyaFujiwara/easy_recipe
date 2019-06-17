from datetime import date, datetime

# date, datetimeの変換関数
def datetime_serial(obj):
    # 日付型の場合には、文字列に変換
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

    raise TypeError ("Type %s not serializable" % type(obj))