# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, template='Hello, <name>!'):
    template = template.replace('<name>', name)
    return template
    
def force(mass, body='earth' ):
    bodies = {
        'sun' : 274,
        'jupiter' : 24.92,
        'neptune' : 11.15,
        'saturn' : 10.44,
        'earth' : 9.798,
        'uranus' : 8.87,
        'venus' : 8.87,
        'mars' : 3.71,
        'mercury' : 3.7,
        'moon' : 1.62,
        'pluto' : 0.58
    }
    gravity = bodies[body.lower()]
    return mass * round(gravity, 1)
    
def pull(m1,m2,d):
    G = 6.674*10**-11
    return G * ((m1*m2)/d**2)
