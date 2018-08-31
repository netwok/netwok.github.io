#Papers, Please - CodeWars

class Inspector(object):
    def __init__(self):
        self.allowed = set([])
        self.date = 19821122
        self.countries = ['Arstotzka', 'Antegria', 'Impor', 'Kolechia', 'Obristan', 'Republia', 'United Federation']
        self.polio = set([])
        self.tetanus = set([])
        self.passport = False
        self.ID = set([])
        self.permit = set([])
        self.work_pass = set([])
        self.grant_of_asylum = set([])
        self.certificate_of_vaccination = set([])
        self.diplomatic_authorization = set([])
        
    def receive_bulletin(self, message):
        print(bulletin)
        self.outlaw = ''
        mess = message.split('\n')
        for line in mess:
            if 'Allow' in line:
                start = line.find('of ') + 3
                self.allowed.update(line[start:].split(', '))
            if 'Deny' in line:
                start = line.find('of ') + 3
                self.allowed = self.allowed.difference(line[start:].split(', '))
            if 'Wanted' in line:
                self.outlaw = line[line.find(': ') + 2:]
            if 'polio' in line:
                if 'no longer' in line:
                   self.polio = set([])
                else:
                    start = line.find('of ') + 3
                    c = line[start:line.find(' req')].split(', ')
                    self.polio.update(c)
            if 'tetanus' in line:
                if 'no longer' in line:
                   self.tetanus = set([])
                else:
                    start = line.find('of ') + 3
                    c = line[start:line.find(' req')].split(', ')
                    self.tetanus.update(c)
            if "passport" in line:
                self.passport = 'no' not in line
            if "ID" in line:
                start = line.find('of ') + 3
                c = line[start:line.find(' req')].split(', ')
                self.ID.update(c)
            if 'permit' in line:
                start = line.find('of ') + 3
                c = line[start:line.find(' req')].split(', ')
                self.permit.update(c)
            if 'work pass' in line:
                start = line.find('of ') + 3
                c = line[start:line.find(' req')].split(', ')
                self.work_pass.update(c)
            if 'asylum' in line:
                start = line.find('of ') + 3
                c = line[start:line.find(' req')].split(', ')
                self.grant_of_asylum.update(c) 
            if 'diplomatic' in line:
                start = line.find('of ') + 3
                c = line[start:line.find(' req')].split(', ')
                self.diplomatic_authorization.update(c)

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
        self.name = set(self.get_detail(self.description[doc], 'NAME: ') for doc in self.docs)
        self.ID = set(self.get_detail(self.description[doc], 'ID#: ') for doc in self.docs)
        self.DOB = set(self.get_detail(self.description[doc], 'DOB: ') for doc in self.docs)
        self.nation = set(self.get_detail(self.description[doc], 'NATION: ') for doc in self.docs)
        self.EXP = set(self.get_detail(self.description[doc], 'EXP: ') for doc in self.docs)
        self.sex = set(self.get_detail(self.description[doc], 'SEX: ') for doc in self.docs)
        
    
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

inspector = Inspector()
bulletin2 = """Entrants require passport
Allow citizens of Arstotzka, Obristan
Citizens of Arstotzka, Obristan require polio vaccination"""

inspector.receive_bulletin(bulletin2)


