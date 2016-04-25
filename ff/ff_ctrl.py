#!/usr/bin/python
"""
ff control
"""
import os, time, re
from static_content import *
__version__ = 0.2

options = {}

HOME_PATH = os.environ["HOME"]
#BASHRC_PATH = HOME_PATH + '/.bashrc'
BASHRC_PATH = HOME_PATH + '/.bash_profile'
FFRC_PATH = HOME_PATH + '/.ffrc'
VIMRC_PATH = HOME_PATH + '/.vimrc'

ACTION_INSTALL = 'install'
ACTION_VIM_SETUP = 'vimsetup'
ACTION_HELP = 'help'

def printHelp():
  print 'Example:'
  print 'ff_ctrl action [--params ...]'
  print '''
      Actions:
        install : install ff script'''

def install():
  print 'Installing ff script...'
  #print 'Dry run:' + str(options.dryrun)

  bashrcExist = os.path.exists(BASHRC_PATH)
  ffrcExist = os.path.exists(FFRC_PATH)
  if not bashrcExist:
    print 'Bash profile does not exsit, creating it first...'
    printRun('touch ' + BASHRC_PATH)

  if ffrcExist:
    print '~/.ffrc already exist. Overriding...'
    createFFRC()
    appendFFRC2bash()
  else:
    print 'Creating ~/.ffrc'
    createFFRC()
    appendFFRC2bash()

def printRun(cmd):
  print cmd
  assert os.system(cmd) == 0

def writeContent(filePath, content):
  fd = open(filePath, "w");
  fd.write(content)
  fd.close()

def createFFRC():
  writeContent(FFRC_PATH, FFRC_CONTENT)
  printRun('. ~/.ffrc')

def appendFFRC2bash():
  fd = open(BASHRC_PATH, "r")
  lines = fd.readlines()
  hasFFRCappend = len([x for x in lines if 'ZHIFENG_FF_PLUGIN_START' in x or 'ZHIFENG_FF_PLUGIN_END' in x ]) == 2
  if hasFFRCappend:
    print 'FFRC append already exist'
  else:
    print 'Appending FFRC to bash profile'
    with open(BASHRC_PATH, "a") as myfile:
      myfile.write(FFRC_APPENDIX)

  print 'Setup completed, please reload bash profile.'

def vimSetup():
  writeContent(VIMRC_PATH, VIMRC_CONTENT)
  print 'VIMRC created'

def main():
  from optparse import OptionParser
  parser = OptionParser()
  #parser.add_option('--dry', dest='dryrun', action='store_true', help='dry run')

  (opts,args) = parser.parse_args()
  global options
  options = opts
  print 'options:', options
  print 'args:', args
  print '\n\n'

  if (len(args) == 0):
    parser.print_help()
    printHelp()
    exit()

  action = args[0]
  # action that target a single app
  ALL_ACTION = {
             ACTION_INSTALL: install,
             ACTION_VIM_SETUP : vimSetup,
             ACTION_HELP: printHelp
  }

  if action in ALL_ACTION:
    ALL_ACTION[action](*args[1:])
    print ('\n\n')
    exit(0)
  else:
    printHelp()

if __name__ == '__main__':
  main()
