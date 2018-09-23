<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
      <title>HRIS - DEVELOP</title>
    {% endblock %}
</head>
<body>
 {% include '_navbar.html' %}
    <div class="container">
        {% block body %}{% endblock %}
    </div>
 <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>

</body>
</html>