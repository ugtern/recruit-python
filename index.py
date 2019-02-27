import bjoern
from wsgirouter import Router

from app import App

app = App()

router = Router()
router.route('/', ['POST'])(app.save)
router.route('/', ['GET'])(app.show)
bjoern.run(router, '0.0.0.0', 8080)
