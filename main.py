true_values = ['yes', 'y']
false_values = ['no', 'n']


def str2bool(value):
    value = value.lower()
    if  value in true_values:
        return True
    if value in false_values:
        return False
    raise ValueError("Tipo erroneo")

try:
    print(str2bool("1"))
except Exception as ex:
    print(Exception)
    