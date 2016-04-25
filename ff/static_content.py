"""
Static content
"""

FFRC_CONTENT = '''#!/bin/bash
############################## ZHIFENG ffrc START #####################
# FFRC Version 0.1

if [ "$(uname)" = Darwin ]; then
  export __FF_OS_TYPE=MACOS
else
  export __FF_OS_TYPE=LINUX
fi

# Function key binding
if [ -z "$__FF__BIND_FUNC_KEY" ]; then
  echo
else
  if [ $__FF_OS_TYPE == MACOS ]; then
    bind '"\eOP":"vim $F1\\015"'
    bind '"\eOQ":"vim $F2\\015"'
    bind '"\eOR":"vim $F3\\015"'
    bind '"\eOS":"vim $F4\\015"'
    bind '"\e[15~":"vim $F5\\015"'
    bind '"\e[17~":"vim $F6\\015"'
    bind '"\e[18~":"vim $F7\\015"'
    bind '"\e[19~":"vim $F8\\015"'
    bind '"\e[20~":"vim $F9\\015"'
    bind '"\e[21~":"vim $F10\\015"'
    __FF__BIND_FUNC_KEY=1
  else
    bind '"\eOP":"vim $F1\\n"'
    bind '"\eOQ":"vim $F2\\n"'
    bind '"\eOR":"vim $F3\\n"'
    bind '"\eOS":"vim $F4\\n"'
    bind '"\e[15~":"vim $F5\\n"'
    bind '"\e[17~":"vim $F6\\n"'
    bind '"\e[18~":"vim $F7\\n"'
    bind '"\e[19~":"vim $F8\\n"'
    bind '"\e[20~":"vim $F9\\n"'
    bind '"\e[21~":"vim $F10\\n"'
    __FF__BIND_FUNC_KEY=1
  fi
fi

# Quick alias
alias rf1='load_file $F1'
alias rf2='load_file $F2'
alias rf3='load_file $F3'
alias rf4='load_file $F4'
alias rf5='load_file $F5'
alias rf6='load_file $F6'
alias rf7='load_file $F7'
alias rf8='load_file $F8'
alias rf9='load_file $F9'

alias v1='vim $F1'
alias v2='vim $F2'
alias v3='vim $F3'
alias v4='vim $F4'
alias v5='vim $F5'
alias v6='vim $F6'
alias v7='vim $F7'
alias v8='vim $F8'
alias v9='vim $F9'

# Main utt function
function source_file() {
  if [ $# -lt 1 ] ; then
    TARGET=.
  else
    TARGET=$1
  fi
  find $TARGET -type d \( -path "*/.svn" -o -path "*/build" -o -path "*/.git"  \) -prune -o \
  -type f \( -iname "tags" \) -prune -o -type f -size +100000c -prune -o -type f -exec grep -Il . {} \;
}

_mapff() {
  i=1
  export __all_ff=$* 
  for file in $* 
  do
    if ((i % 2 == 0))
    then
      printf "\e[1;32m"
    fi
    export F$i=$file
    echo "[F$i]" $file 
    let " i+= 1"
    printf "\e[0m"
  done
}

_ff() {
# \* escaping the asterisk avoid shell expanding
  find . -name \*"$1"\* -o -type d \( -path "*/build" -o -path "*/.svn" -o -path "*/zip" -o -path "*/.git" \) -prune | egrep -v "./build|.git|.svn|./zip"
}

_ffb() {
  find . -name \*"$1"\* -o -type d \( -path "*/.svn" -o -path "*/.git" \) -prune | egrep -v ".git|.svn"
}

ff() {
  if [ $# -lt 1 ] ; then
    echo "usage: ff pattern"
    return
  fi
  _mapff `_ff $*`
}

ffb() {
  if [ $# -lt 1 ] ; then
    echo "usage: ffb pattern"
    return
  fi
  _mapff `_ffb $*`
}

editall () {
  vim $__all_ff
}

function gg() {
  if [ $# -lt 1 ] ; then
    echo "usage: greplg keyword"
    return
  fi
  source_file | xargs -I "fn" grep "$1" -n -B 2 --with-filename -A 2 --color=auto "fn"
}

function ggg() {
  if [ $# -lt 1 ] ; then
    echo "usage: greplg keyword"
    return
  fi
  source_file $WP | xargs -I "fn" grep "$1" -n -B 2 --with-filename -A 2 --color=auto "fn"
}

function gglist() {
  if [ $# -lt 1 ] ; then
    echo "usage: greplg keyword"
    return
  fi
  _mapff `source_file | xargs -I "fn" grep "$1" --with-filename "fn" | cut -d: -f 1 | uniq`
}

gff() {
  if [ $# -lt 1 ] ; then
    echo "usage: ff filepattern"
    return
  fi
  _mapff `find $WP -name \*"$1"\* -o -type d \( -path "*/build" -o -p "*/zip" -o -path "*/.svn" -o -path "*/.git" \) -prune | egrep -v "./build|.git|.svn|./zip" | grep --color $1`
}

load_file() {
  if [ $# -lt 1 ] ; then
    echo "load_file F1 or 1 or filename"
    return
  else
    vim -c ":qa" $1
  fi
}
############################## ZHIFENG ffrc END #####################
'''

FFRC_APPENDIX = '''
########## ZHIFENG_FF_PLUGIN_START #############
if [ -f ~/.ffrc ]; then
  . ~/.ffrc
fi
########## ZHIFENG_FF_PLUGIN_END ##############
'''


VIMRC_CONTENT = '''"                 VIMRC FENGYU05
"
""" Vundle {{{
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Plugin 'tpope/vim-abolish'
Plugin 'vim-scripts/mru.vim'
Plugin 'vim-scripts/taglist.vim'
Plugin 'fholgado/minibufexpl.vim'
Plugin 'rustushki/JavaImp.vim'
Plugin 'ntpeters/vim-better-whitespace'
Plugin 'scrooloose/nerdcommenter'
Plugin 'scrooloose/nerdtree'
Plugin 'kien/ctrlp.vim'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'derekwyatt/vim-scala'
Plugin 'akhaku/vim-java-unused-imports'
Plugin 'tfnico/vim-gradle'
"Plugin 'jvenant/vim-java-imports' " 
"Plugin 'Valloric/YouCompleteMe'


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

"}}}

""" Basic setting {{{
" set line no on
set wildmenu
" Ignore compiled files
set wildignore=*.o,*~,*.pyc
set ruler
set cmdheight=2
" A buffer becomes hidden when it is abandoned
set hid

" Configure backspace so it acts as it should act
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

" Makes search act like search in modern browsers
set incsearch

" Don't redraw while executing macros (good performance config)
set lazyredraw

" For regular expressions turn magic on
set magic

" Show matching brackets when text indicator is over them
set showmatch
" How many tenths of a second to blink when matching brackets
set mat=2

" No annoying sound on errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500

set lbr
set ai "Auto indent
set si "Smart indent
set wrap "Wrap lines

let mapleader = "\\\\"
let g:mapleader = "\\\\"

" No annoying sound on errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500

syntax enable
set nobackup
set nowb
set noswapfile
set smarttab
set expandtab " Force this, although it's in google.vim
set shiftwidth=2 " Force this, although it's in google.vim
set softtabstop=2 " Make tabs act like spaces for editing ops
set wildmode=longest,list,full " Completion modes for wildcard expansion
set hlsearch " Highlight previous search results
set showmode " Show the mode you're currently in
set showmatch " Show matching braces / brackets
set incsearch " Do incremental searching
set number " Set line numbers
set title " Let vim change my tab/window title
set autoread
setlocal textwidth=500
colorscheme elflord
match Label /\s\u\w\+\s/

" highlight kework
nmap # #*

""" end of basic setting }}}

" StatusBar {{{
" Always show the status line
set laststatus=2
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l
set listchars=tab:--,trail:!,extends:>,precedes:<
" StatusBar }}}

" MiniBuffExplorer {{{
let g:miniBufExplModSelTarget = 1
let g:miniBufExplorerMoreThanOne = 0
let g:miniBufExplModSelTarget = 0
let g:miniBufExplUseSingleClick = 1
let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplVSplit = 25
let g:miniBufExplSplitBelow=1

" MiniBuffExplorer End }}}

" JavaImporter {{{
" Run from commandline:
" find "$HOME/workspace" | grep build |  grep -e ".classpath$"  | xargs cat | tr ':' '\\n' | sort | uniq | tr '\\n' ':' > ~/vim/JavaImp/jars"
let javaImportListCmd = "cat " . $HOME . "/vim/JavaImp/jars"
let g:JavaImpPaths = system(javaImportListCmd)
let g:JavaImpPaths .= ":" . $HOME . "/vim/JavaImp/jmplst/jdk.jmplst"
let g:JavaImpDataDir = $HOME."/javaimp_cache"
let g:JavaImpDataDir = $HOME."/javaimp_cache"
let g:JavaImpDocPaths= $HOME."/javadoc"
let g:JavaImpDocViewer = "lynx"
let g:JavaImpTopImports = [ ]

" Import class
nmap <leader>jj :JI<CR>:JIS<CR>
nmap <leader>ji :JI<CR>
nmap <leader>g :JI<CR>
" Sort class import
nmap <leader>js :JIS<CR>
" View file
nmap <leader>jf :JIF<CR>
" Java Doc
nmap <leader>jD :JID<CR>

" JavaImporter end}}}

" window navigation {{{
map <C-h> <C-W>h
map <C-l> <C-W>l
"}}}

" main function key {{{
nmap <F2> :source ~/.vimrc<cr>
nmap <F3> :e ~/.vimrc<cr>
nmap <F4> :bd<cr>
nmap <F5> :Tlist<cr>
nmap <F6> :MRU<cr>
nmap <F7> :set number! number?<cr>
nmap <F8> :set nopaste! nopaste?<cr>
nmap <F9> :call PlainMode()<cr>

nmap <leader><F12> :qa!<cr>
nmap <leader><esc> :qa!<cr>
nmap <leader><delete> :qa!<cr>
nmap <c-`> <esc>
"}}}

" function key alt {{{
imap <F1> <esc><F1>
imap <F2> <esc><F2>
imap <F3> <esc><F3>
imap <F4> <esc><F4>
imap <F5> <esc><F5>
imap <F6> <esc><F6>
imap <F7> <esc><F7>
imap <F8> <esc><F8>
imap <F9> <esc><F9>

" function key alt }}}

" undo and redo <C-u> <C-r> {{{
nmap <C-u> :undo<cr>
nmap u <esc>
" }}}

" word correct {{{
iab pirnt print
" }}}

" scorlling {{{
nmap <C-D> 25j
nmap <C-F> 25k
" Set 7 lines to the cursor - when moving vertically using j/k
set so=7
" }}}

" buff ctrl {{{
nmap <leader>a :e  
nmap <leader>e :e  
nmap <leader>z :ls<cr>

"buff navigation
nmap <Tab> :bn<cr>
nmap <S-Tab> :bp<cr>
" }}}

" NerdTree {{{
nmap <leader>f :NERDTreeFind<cr>
" NERDTree End}}}

" Folder {{{
set foldlevel=1
set foldmethod=syntax
set foldnestmax=10
set nofoldenable

autocmd FileType vim setlocal foldmethod=marker
" }}}

" Plugin CtrlP {{{
let g:ctrlp_map='<leader>p'
let g:ctrlp_max_files=0
let g:ctrlp_custom_ignore = {
      \\'dir': '\\v[V](.git|.hg|.svn|build|_codegen|tmp)$',
      \\'file': '\\v\.(so|class|jar|war|pyc)$',
      \}
let g:ctrlp_clear_cache_on_exit=0
let g:ctrlp_switch_buffer='et'
" }}}

" Snippets {{{
" Snippets are separated from the engine. Add this if you want them:

" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
let g:UltiSnipsExpandTrigger="<c-y>"
"let g:UltiSnipsJumpForwardTrigger="<c-b>"
"let g:UltiSnipsJumpBackwardTrigger="<c-z>"
let g:UltiSnipsListSnippets="<c-l>"


" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"

" Snippets end }}}

" Read .class using javap decompiler {{{
function! s:ReadClass(dir, classname)
  execute "cd " . a:dir
  execute "0read !javap -c " . a:classname
  1
  setlocal readonly
  setlocal nomodified
endfunction
autocmd BufReadCmd *.class call <SID>ReadClass(expand("<afile>:p:h"), expand("<afile>:t:r"))
" End Read .class }}}

""" Pig config {{{
augroup filetypedetect
  au BufNewFile,BufRead *.pig set filetype=pig syntax=pig
augroup END
" }}}

""" Function {{{
" Function begin here, Function mush start with capital letter.
function! HasPaste()
if &paste
return 'PASTE MODE '
en
return ''
endfunction

function! GoogleNit()
execute '!nit.py %'
endfunction

function! FindUniqueWords()
  let stat = {}
  for ii in range(1, line('$'))
    for word in split(getline(ii), '\(\k\@!.\)\+')
      let stat[word] = get(stat, word, 0) + 1
    endfor
  endfor
  let uq_worbs = filter(copy(stat), 'v:val == 1')
  for word in keys(uq_worbs)
  endfor
  echo sort(keys(uq_worbs))
endfunction

function! PlainMode()
set nonu
only
endfunction

function! FindAllTag()
  echo 'FindAllTag'
  echo expand("<cword>")
  ta /expand("<cword>")
endfunction

"}}}
'''

FF_UTT_CONTENT = '''
############################## ZHIFENG ff utt START #####################
# Git utt
alias git_push_origin='git push -u origin master'
alias git_pull_rebase='git pull --rebase'
alias git_commit_amend='git commit --amend'
alias git_checkout_origin='git checkout origin/master'
alias git_list_unpushed='git log origin/master..HEAD --name-only'
alias git_info='git remote show origin'

function git_list_edit() {
  _mapff `git status | grep -E 'new file:|modified:' | cut -d ':' -f 2`
}

# Svn utt

############################## ZHIFENG ffrc END #####################
'''


