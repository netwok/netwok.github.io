#Papers, Please - CodeWars

countries = ['Arstotzka', 'Antegria', 'Impor', 'Kolechia',
'Obristan', 'Republia', 'United Federation']
foreign = ['Antegria', 'Impor', 'Kolechia',
'Obristan', 'Republia', 'United Federation']
vacc = {co:0 for co in countries}
#polio==1, tetanus==2, both==3
req = {co:[] for co in countries}

class Game(object):
    def __init__(self):
        self.allowed = set([])
    
    def receiveBulletin(self, message):
        self.outlaws = set([]) 
        message = message.split('\n')
        for line in message:
            if 'Allow' in line:
                start = line.find('of ') + 3
                self.allowed.update(line[start:].split(', '))
            if 'Deny' in line:
                start = line.find('of ') + 3
                self.allowed = self.allowed.difference(line[start:].split(', '))
            if 'Wanted' in line:
                start = line.find(': ') + 2
                self.outlaws.update(line[start:].split(', '))
            if 'permit' in line:
                pass
            if 'polio' in line:
                if 'no longer' in line:
                   start = line.find('of ') + 3 
                
    def inspect(self, entrant):
        #first check the names for criminals
        #if outlaws in entrant.names: return 'Detained etc.'
        #if len(entrant.names) > 1 or len(entrant.DOBs) > 1 or...: return 'False Documents etc.'
        #if documents expired: return 'yadda yadda'
        #for doc in req:
        # yadda yadda
        pass


class Entrant(object):
    def __init__(self, description):
        self.description = description
        self.docs = description.keys()
        self.passport = description.get('passport', False)
        self.ID_card = description.get('ID_card', False)
        self.access_permit = description.get('access_permit', False)
        self.work_pass = description.get('work_pass', False)
        self.grant_of_asylum  = description.get('grant_of_asylum', False)
        self.certificate_of_vaccination  = description.get('certificate_of_vaccination', False)
        self.diplomatic_authorization  = description.get('diplomatic_authorization', False)
        
        self.names = set(self.get_detail(self.description[doc], 'NAME: ') for doc in self.docs)
        self.IDs = set(self.get_detail(self.description[doc], 'ID#: ') for doc in self.docs)
        self.DOBs = set(self.get_detail(self.description[doc], 'DOB: ') for doc in self.docs)
        self.nations = set(self.get_detail(self.description[doc], 'NATION: ') for doc in self.docs)
        
    
    def get_detail(self, doc, code):
        start = doc.find(code) + len(code)
        n = doc[start:doc.find('\n', start)]
        if ',' not in n:
            return n
        else:
            return ' '.join(n.split(', ')[::-1])
         
        
entrant1 = {
"passport": """ID#: GC07D-FU8AR
NATION: Arstotzka
NAME: Guyovich, Russian
DOB: 1933.11.28
SEX: M
ISS: East Grestin
EXP: 1983.07.10"""
}
roman = {
	"passport": 'ID#: WK9XA-LKM0Q\nNATION: United Federation\nNAME: Dolanski, Roman\nDOB: 1933.01.01\nSEX: M\nISS: Shingleton\nEXP: 1983.05.12',
	"grant_of_asylum": 'NAME: Dolanski, Roman\nNATION: United Federation\nID#: Y3MNC-TPWQ2\nDOB: 1933.01.01\nHEIGHT: 176cm\nWEIGHT: 71kg\nEXP: 1983.09.20'
}
entrant = Entrant(roman)
