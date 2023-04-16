FROM redis:7.2-rc1-bullseye

RUN apt-get update \
    && apt-get install -y vim \
    && apt-get install git -y \
    && git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim \
    && rm -rf /var/lib/apt/lists/*

COPY .vimrc /root/.vimrc
