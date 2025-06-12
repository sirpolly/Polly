-- Включить взаимодействие с мышью
vim.o.mouse = 'a'

-- Включить нумерацию строк
vim.wo.number = true

-- Включить относительную нумерацию строк
vim.wo.relativenumber = false

-- Включить "умные" табы (автоматическое добавление пробелов вместо табуляции)
vim.o.smarttab = true

-- Установить ширину таба и отступов в 2 пробела
-- vim.o.tabstop = 2
-- vim.o.shiftwidth = 2
-- vim.o.softtabstop = 2

-- Включить автоматический отступ при новых строках
vim.o.autoindent = true

-- Включение нумерации строк
-- vim.opt.number = true

-- Включение отображения текущей строки
vim.opt.cursorline = true

-- Включение подсветки строки с курсором
vim.opt.showmatch = true

-- Настройка отступов
vim.opt.expandtab = true      -- Использовать пробелы вместо табов
vim.opt.shiftwidth = 4        -- Размер отступа в пробелах
vim.opt.tabstop = 4           -- Размер таба в пробелах

-- Включение линий сетки (опционально)
-- vim.opt.relativenumber = true -- Относительная нумерация (для удобства навигации)

-- Другие полезные настройки
vim.opt.smartindent = true
vim.opt.wrap = false

-- Можно добавить дополнительные настройки по желанию

vim.cmd[[colorscheme ron]]

-- Перемещаем имя файла сверху
-- vim.o.winbar = "%f"
vim.api.nvim_set_hl(0, 'WinBar', { fg = '#000000', bg = '#99ccff' })

-- Увеличиваем высоту командной строки примерно вдвое
vim.o.cmdheight = 2

-- Устанавливаем цвет статусной строки светло-голубым фоном
-- vim.api.nvim_set_hl(0, 'StatusLine', { fg = '#000000', bg = '#cceeff' })

-- Включаем глобальную статусную линию внизу
vim.o.laststatus = 2

-- Увеличиваем высоту командной строки
-- vim.o.cmdheight = 4

-- Устанавливаем цвет статусной строки светло-голубым фоном и чёрным текстом
vim.api.nvim_set_hl(0, 'StatusLine', { fg = '#000000', bg = '#cceeff' })

-- Включаем глобальную статусную линию
-- vim.o.laststatus = 3

-- Настраиваем строку с курсором (например, для подсветки строки курсора)
-- Можно изменить цвет фона или текста курсора
vim.api.nvim_set_hl(0, 'CursorLine', { fg = 'NONE', bg = '#ff69b4' }) -- розовый фон для текущей строки

-- Также можно настроить подсветку позиции курсора (например, для строки или столбца)
vim.api.nvim_set_hl(0, 'CursorColumn', { fg = 'NONE', bg = '#ff69b4' }) -- розовый фон для столбца с курсором

vim.cmd('highlight StatusLine guifg=#000000 guibg=#cceeff')
vim.cmd('highlight CursorLine guibg=#ff69b4')

vim.o.clipboard = 'unnamedplus'


-- 1. Инициализация Packer (ДОЛЖЕН БЫТЬ ПЕРВЫМ И ЕДИНСТВЕННЫМ return В ФАЙЛЕ)
vim.cmd [[packadd packer.nvim]]

require('packer').startup(function(use)
  use 'wbthomason/pucker.nvim'
  -- Другие плагины...
  
  -- Плагин для поддержки LSP и автодополнения
  use 'neovim/nvim-lspconfig'
  
  -- Плагин для автодополнения
  use 'hrsh7th/nvim-cmp'
  use 'hrsh7th/cmp-nvim-lsp'
  
  -- Плагин для подсветки ошибок и linting
  use 'mfussenegger/nvim-lint'
  
  -- Плагин для форматирования кода
  use 'jose-elias-alvarez/null-ls.nvim'
end)

return require('packer').startup(function(use)
  -- Плагины
  use 'wbthomason/packer.nvim' -- Менеджер плагинов

  -- LSP
  use 'neovim/nvim-lspconfig'
  use 'williamboman/mason.nvim'
  use 'williamboman/mason-lspconfig.nvim'

  -- Автодополнение
  use 'hrsh7th/nvim-cmp'
  use 'hrsh7th/cmp-nvim-lsp'
  use 'L3MON4D3/LuaSnip'

  -- Python
  use 'python-mode/python-mode'
  use 'Vimjas/vim-python-pep8-indent'
end)
-- КОНЕЦ БЛОКА PACKER (ниже идут настройки)


vim.o.clipboard = 'unnamedplus'

vim.g.clipboard = {
  name = 'win32yank',
  copy = {
    ['+'] = 'C:\\tools\\win32yank\\win32yank.exe -i --crlf',
    ['*'] = 'C:\\tools\\win32yank\\win32yank.exe -i --crlf',
  },
  paste = {
    ['+'] = 'C:\\tools\\win32yank\\win32yank.exe -o --crlf',
    ['*'] = 'C:\\tools\\win32yank\\win32yank.exe -o --crlf',
  },
  -- cache_enabled = true,
}

vim.o.clipboard = 'unnamedplus'

vim.g.clipboard = {
  name = 'win32yank',
  copy = {
    ['+'] = 'C:\\tools\\win32yank\\win32yank.exe -i --crlf',
    ['*'] = 'C:\\tools\\win32yank\\win32yank.exe -i --crlf',
  },
  paste = {
    ['+'] = 'C:\\tools\\win32yank\\win32yank.exe -o --crlf',
    ['*'] = 'C:\\tools\\win32yank\\win32yank.exe -o --crlf',
  },
}

-- Использовать системный буфер обмена (если Neovim поддерживает clipboard)
vim.opt.clipboard:append("unnamedplus")  -- Теперь y/p используют системный буфер

-- Горячие клавиши для удобства (Ctrl+C / Ctrl+V)
vim.api.nvim_set_keymap("v", "<C-c>", '"+y', { noremap = true, silent = true })      -- Копировать выделенное
vim.api.nvim_set_keymap("n", "<C-v>", '"+p', { noremap = true, silent = true })      -- Вставить в Normal mode
vim.api.nvim_set_keymap("i", "<C-v>", '<C-o>"+p', { noremap = true, silent = true }) -- Вставить в Insert mode

-- Функция для вставки из буфера Windows
local function paste_from_clipboard()
  local clipboard = vim.fn.system('win32yank -o --lf')
  vim.api.nvim_put({ clipboard }, '', false, true)
end

-- Маппинг для вставки (например, на Ctrl+V)
vim.api.nvim_set_keymap('n', '<C-v>', '<cmd>lua paste_from_clipboard()<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('i', '<C-v>', '<Esc><cmd>lua paste_from_clipboard()<CR>gi', { noremap = true, silent = true })

vim.api.nvim_set_keymap('n', '<Leader>p', ':r !win32yank -o<CR>', { noremap = true, silent = true })

-- 1. Настройка буфера обмена с win32yank:
-- lua
vim.g.clipboard = {
  name = 'win32yank',
  copy = {
    ['+'] = 'win32yank -i --crlf',
    ['*'] = 'win32yank -i --crlf',
  },
  paste = {
    ['+'] = 'win32yank -o --lf',
    ['*'] = 'win32yank -o --lf',
  },
  cache_enabled = false,
}

-- Вставка содержимого буфера в текущую позицию
vim.api.nvim_create_user_command('Paste', function()
  local clipboard = vim.fn.system('win32yank -o')
  vim.api.nvim_put({clipboard}, '', false, true)
end, {})

-- Вставка содержимого буфера на новую строку
vim.api.nvim_create_user_command('PasteLine', function()
  local clipboard = vim.fn.system('win32yank -o')
  vim.api.nvim_put({clipboard}, 'l', false, true)
end, {})


-- Установка опций для Python-разработки
vim.bo.tabstop = 4       -- 4 пробела на таб
vim.bo.softtabstop = 4   -- 4 пробела при нажатии Tab
vim.bo.shiftwidth = 4    -- 4 пробела для autoindent
vim.bo.expandtab = true  -- Использовать пробелы вместо табов
vim.bo.autoindent = true -- Автоотступы

-- Включение подсветки синтаксиса
vim.cmd('syntax enable')
vim.cmd('filetype plugin indent on')

-- Автодополнение при вводе
vim.opt.completeopt = {'menuone', 'noselect', 'noinsert'}
vim.opt.shortmess:append('c')  -- Убрать лишние сообщения


-- 2. Общие настройки (после return)
vim.o.number = true
vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.expandtab = true

-- 3. Настройка LSP
require('mason').setup()
require('mason-lspconfig').setup({
  ensure_installed = {'pyright'}
})

require('lspconfig').pyright.setup({})

-- 4. Настройка автодополнения
local cmp = require('cmp')
cmp.setup({
  sources = {
    {name = 'nvim_lsp'},
    {name = 'luasnip'}
  }
})

-- 5. Горячие клавиши
vim.keymap.set('n', '<F5>', ':w<CR>:!python %<CR>', {silent = true})
vim.keymap.set('n', 'gd', vim.lsp.buf.definition, {})

-- 6. Python-специфичные настройки
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'python',
  callback = function()
    vim.opt_local.colorcolumn = '88'
	end)
})
end)