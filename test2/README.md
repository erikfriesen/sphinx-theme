# Slide Custom CSS example

This is an example of how to add boundless branding to a sphinx using custom css rather than a theme.

In `config.py`:
```
slide_theme_options = {'custom_css': 'boundless_slides.css'}
```

For this to work section breaks are marked:

```
.. rst-class:: section

Style Guidelines
================
```

This allows the default `slides` and `single_level` slide themes to work out of the box without modification.

## Building

To try out the slide functionality:

```
ant slides
```

To generate `html` a target is setup for each theme:

```
ant learning
```

```
ant server
```

```
ant rtd
```


PDF output requires pdflatex:

```
ant pdf
```

For the complete list of build targets:

```
ant -p 
```
