from distutils.core import setup
import setup_translate

pkg = 'Extensions.CacheFlush'
setup (name = 'enigma2-plugin-extensions-cacheflush',
       version = '1.10',
       description = 'periodicaly flush box cache',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['*.png', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
