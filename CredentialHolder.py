

class CredentialHolder:
    def __init__(self):
        self.stuff = dict()
        self.len = 0
    def insert(self, username, password):
        if username in self.stuff:
            if password in self.stuff[username]:
                #print('[WARNING]' + username + ':' + password + ' already exists')
                return
            self.stuff[username].append(password)
        else:
            self.stuff[username] = [password]
        self.len += 1
    def exists(self, username, password):
        if username in self.stuff:
            return password in self.stuff[username]
        return False
