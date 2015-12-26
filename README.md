# django-jsdata

A small Django utility for transporting data from views to JavaScript variables.


## Installation

The usual, add `jsdata` to `INSTALLED_APPS`.


## Using in Views

```python
from jsdata.views import JSDataViewMixin

class HomeView(JSDataViewMixin, TemplateView):
    template_name = 'index.html'

    def get_jsdata(self, **kwargs):
        data = {
            'hello': 'world',
            'sub': {
                'value': 4,
            }
        }
        data.update(kwargs)
        return super(HomeView, self).get_jsdata(**data)
```


## Using in Templates

```html
{% load jsdata %}

<html>
  <head>
    <script src="{% static 'js/jsdata.js' %}"></script>
    {% jsdata %}
  </head>
  <body>
  </body>
</html>
```


## Using in JavaScript

```javascript
console.log( jsdata( 'world' ) ); // world
console.log( jsdata( 'sub.data' ) ); // 4
console.log( jsdata( 'invalid', 'default' ) ); // default
```
