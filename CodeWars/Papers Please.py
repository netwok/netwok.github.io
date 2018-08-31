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
        print(message)
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
    
    def detain(self, code):
        return "Detainment: {} mismatch.".format(code)
        
    def deny(self, code):
        return "Entry denied: missing required {}.".format(code)
    
    def inspect(self, entrant):
        print('entrant: ',entrant)
        entrant = Entrant(entrant)
        if self.outlaw:
            if self.outlaw in entrant.name:
                return "Detainment: Entrant is a wanted criminal."
        if len(entrant.name) > 1:
            return self.detain("name")
        if len(entrant.ID) > 1:
            return self.detain("ID number")
        if len(entrant.DOB) > 1:
            return self.detain("DOB")
        if len(entrant.nation) > 1:
            return self.detain("nation")
        if len(entrant.sex) > 1:
            return self.detain("sex")
        if entrant.nation in self.polio:
            #if 
            return self.deny("vaccination")
        if self.passport:
            if 'passport' not in entrant.docs:
                return self.deny('passport')
        if entrant.nation not in self.allowed:
            if entrant.nation != {"Arstotzka"} and 'access_permit' not in entrant.docs:
                return 'Entry denied: citizen of banned nation.'
            
        #OK, let 'em through.
        if entrant.nation == {"Arstotzka"}:
            return 'Glory to Arstotzka.'
        else:
            return "Cause no trouble."
            
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
        self.name = set(self.get_detail(self.description[doc], 'NAME: ') for doc in self.docs if 'NAME: ' in self.description[doc])
        self.ID = set(self.get_detail(self.description[doc], 'ID#: ') for doc in self.docs if 'ID#: ' in self.description[doc])
        self.DOB = set(self.get_detail(self.description[doc], 'DOB: ') for doc in self.docs if 'DOB: ' in self.description[doc])
        self.nation = set(self.get_detail(self.description[doc], 'NATION: ') for doc in self.docs if 'NATION: ' in self.description[doc])
        self.EXP = set(self.get_detail(self.description[doc], 'EXP: ') for doc in self.docs if 'EXP: ' in self.description[doc])
        self.sex = set(self.get_detail(self.description[doc], 'SEX: ') for doc in self.docs if 'SEX: ' in self.description[doc])
        
    
    def get_detail(self, doc, code):
        start = doc.find(code) + len(code)
        n = doc[start:doc.find('\n', start)]
        if ',' not in n:
            return n
        else:
            return ' '.join(n.split(', ')[::-1])
         

bullet = """Allow citizens of Antegria, Impor, Kolechia, Obristan, Republia, United Federation
Wanted by the State: Andre Karlsson"""

i = Inspector()
i.receive_bulletin(bullet)

i.allowed
x = {'passport': 'ID#: M0RWI-H4F5Z\nNATION: Impor\nNAME: Dahl, Natalya\nDOB: 1954.10.04\nSEX: F\nISS: Tsunkeido\nEXP: 1983.07.08'}
