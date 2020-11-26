import datetime
class Tesohh():
    def getFullName(self):
        return('Simone Tesini')
    def getDescription(self):
        return("hi, i'm an italian programmer that is learning. I like to code games and small utilities.")
    def getAge(self):
        # grazie Matteo Peretto
        nowDate = datetime.date.today()
        birthday = datetime.datetime.strptime("Aug 19 2006", "%b %d %Y").date()
        age = int(abs(nowDate - birthday).days / 365)
        return(str(age) + (' yo'))
    def getPhoto(self):
        return('tesohh.jpg')
    def getHobbies(self):
        return(['Programming', 'Videogames'])
    def getSkills(self):
        return({
            'python': '60%',
            'js': '10%',
            'c++/arduino': '15%',
            'design': '20%',
            'webdevelopment': '1%',
            'vim': '2%',
            'git': '15%',
            'linux': '3%',
            'presenting': '80%'
        })
    def getProjects(self):
        return('La Fabbrica dei Cybercani', 'Passbot', 'Project AV', 'Tronk')
        
    def getGitHub(self):
        return('https://github.com/Tesohh')
