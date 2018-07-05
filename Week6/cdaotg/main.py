import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content=-Type'] = 'text/html; charset=UTF-8'
        self.response.write('<title>cdaotg</title>')
        self.response.write('<body><h2>こんにちは！Let\'s play a game ^o^ !</h2>')
        self.response.write('<h1 style="color:#E6675C">Please input two words.</h1>')
        self.response.write('<form><h2><input type ="text" name="a"></h2>')
        self.response.write('<h2>Add: <input type = submit></h2>')
        self.response.write('<form><h2><input type ="text" name="b"><hr></form></h2>')

        
        len_a = len(self.request.get("a"))
        len_b = len(self.request.get("b"))
        a = self.request.get("a")
        b = self.request.get("b")
        
        self.response.write('<h2>Result: ')
        if len_a == len_b:
            for i in range(len_a):
                self.response.write('<b style="color:#FF9999">%s</b><b style="color:#55AEF2">%s</b>' % (a[i],b[i]))
        elif len_a > len_b:
            for i in range(len_b):
                self.response.write('<b style="color:#FF9999">%s</b><b style="color:#55AEF2">%s</b>' % (a[i],b[i]))
            self.response.write('<b style="color:#FF9999">%s</b>' % a[len_b:len_a])
        else:
            for i in range(len_a):
                self.response.write('<b style="color:#FF9999">%s</b><b style="color:#55AEF2">%s</b>' % (a[i],b[i]))
            self.response.write('<b style="color:#55AEF2">%s</b>' % b[len_a:len_b])
        self.response.write('</h2></body>')


app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ], debug = True)
