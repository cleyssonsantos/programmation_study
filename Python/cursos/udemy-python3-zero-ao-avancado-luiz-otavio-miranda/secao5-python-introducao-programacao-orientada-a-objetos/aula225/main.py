# from log import LogPrintMixin, LogFileMixin

# lp = LogPrintMixin()
# lp.log_error("Qualquer Coisa")
# lp.log_success("Que Legal")
# lf = LogFileMixin()
# lf.log_error("Qualquer Coisa")
# lf.log_success("Que Legal")
from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()