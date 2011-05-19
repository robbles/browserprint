" browserprint.vim
" Copyright 2011 Rob O'Dwyer. All rights reserved.
"
" Redistribution and use in source and binary forms, with or without
" modification, are permitted provided that the following conditions are met:
"
" 1. Redistributions of source code must retain the above copyright notice,
"    this list of conditions and the following disclaimer.
" 2. Redistributions in binary form must reproduce the above copyright notice,
"    this list of conditions and the following disclaimer in the documentation
"    and/or other materials provided with the distribution.
"
" THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
" IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
" ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE
" LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
" CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
" SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
" INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
" CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
" ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
" POSSIBILITY OF SUCH DAMAGE.

" Load python module
let s:script_dir=expand("<sfile>:p:h")
python << EOF
import vim, sys
path = vim.eval('s:script_dir')
sys.path.insert(0, path)
import browserprint
# FIXME
reload(browserprint)
sys.path.pop(0)
EOF

" Warning if python support is missing
function! s:BrowserPrintPythonWarning()
  echohl WarningMsg
  echo "browserprint.vim requires Vim to be compiled with Python support"
  echohl none
endfunction

function! s:BrowserPrint()
  if has('python')
    python browserprint.load_buffer(vim.current.buffer)
  else
    call s:BrowserPrintPythonWarning()
  endif
endfunction
command! BrowserPrint call s:BrowserPrint()

