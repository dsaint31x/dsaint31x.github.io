---
title: 'The install of Jekyll on Debian 9'
date: 2019-08-26
permalink: /posts/2012/08/blog-post-1/
tags:
  - jekyll 
  - ruby
  - debian
---

This post will show the steps of installing Jekyll and Ruby on a Debian 9.
Jeykyll is one of the popular static page publication S/W and based on the Ruby.

## Prerequirements

* Debian 9 (Docker image)

## Install Ruby 2.5.x

* The easiest way to install Ruby on your Debian9 is through the `apt` package manager.
* However, `apt` Repository of Debian9 currently provides Ruby **2.3.3**.
* So, this post uses `Rbenv` which is a lightweight Ruby version management tool and allows you to easily switch Ruby versions.
* But, `Rbenv` doesn't cover installation of Ruby by default. 
* So, you need `ruby-build` which helps you to install any version you may need and is available as plugin for rbenv.

* Install the dependencies required for the `ruby-build` and `Ruby` 
```bash
sudo apt update
sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev
curl -sL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-installer | bash -
```   

* Before starting using `rbenv` we need to add `$HOME/.rbenv/bin` to your `$PATH`.
```bash
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

* Now that `rbenv` is installed on your Debian9 we can install the stable version Ruby.
```bash
rbenv install 2.5.1
rbenv global 2.5.1
ruby --version
```

## Install Jekyll
* Now you can install `jekyll`
```bash
gem install jekyll bundler
jekyll --version
```

* Test your installation by installing new test site of jekyll.
```bash
jekyll new [test_site_name]
cd [test_site_name]
jekyll serve --host 0.0.0.0
```

> Note that you should use 0.0.0.0 when jekyll is running through Docker.

