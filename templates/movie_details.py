{% extends "index.html" %}

{% block content %}

<h1 class="my-4">{{ movie.title }}</h1>

<div class="row">
    <div class="col-md-8">
        <img class="img-fluid rounded" src="{{ tmdb_image_url(movie.backdrop_path, 'w780') }}" alt="{{ movie.title }}">
    </div>
    <div class="col-md-4">
        <h4>{{ movie.tagline }}</h4>
        <p>{{ movie.overview }}</p>
        <dl>
            <dt>Budżet</dt>
            <dd>{{ movie.budget }}</dd>
            <dt>Gatunki</dt>
            <dd>{% for genre in movie.genres %}{{ genre.name }}{% if not loop.last %}, {% endif %}{% endfor %}</dd>
        </dl>
        <a href="/" class="btn btn-secondary">← Wróć</a>
    </div>
</div>

<h3 class="my-4">Obsada</h3>
<div class="row">
    {% for actor in cast %}
    {% if actor.profile_path %}
    <div class="col-md-2 col-sm-4 mb-4 text-center">
        <img src="{{ tmdb_image_url(actor.profile_path, 'w185') }}" class="img-fluid rounded" alt="{{ actor.name }}">
        <p class="mt-2"><strong>{{ actor.name }}</strong><br><small class="text-muted">{{ actor.character }}</small></p>
    </div>
    {% endif %}
    {% endfor %}
</div>

{% endblock %}