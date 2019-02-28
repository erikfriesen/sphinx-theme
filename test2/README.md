# Slide Custom CSS example

This is an example of how to add boundless slide branding to a sphinx using custom css in the project (rather than a theme).

In `config.py`:
```
slide_theme_options = {'custom_css': 'boundless_slides.css'}
```

For this to work section breaks are marked:

```
.. rst-class:: section
```

## Style Guidelines

This allows the default `slides` and `single_level` slide themes to work out of the box without modification:

```
_static/boundless_slides.css
_static/cover.png
_static/backgroundblue.png
_static/backgroundblueslide.png
```

## Building

To try out the slide functionality:
```
ant default
```

To build `slides` with your choice of `html` theme:

```
ant slides learning
```

```
ant slides server
```

```
ant slides rtd
```

PDF output requires pdflatex:

```
ant pdf
```

For the complete list of build targets:

```
ant -p 
```
