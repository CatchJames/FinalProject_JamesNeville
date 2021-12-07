$(document).ready(function () {
    $('button').click(function () {

        // Clear before adding in case the user clicks the button twice
        $('#results').empty();

        // Get the search
        const movie_title = $('input[name=movie_title]').val();

        $.ajax({
            "async": true,
            "crossDomain": true,
            "s": movie_title,
            "url": "https://movie-database-imdb-alternative.p.rapidapi.com/?s=Jaws&r=json&page=1",
            "method": "GET",
            "headers": {
                "x-rapidapi-host": "movie-database-imdb-alternative.p.rapidapi.com",
                "x-rapidapi-key": "2079658137mshae024564d054edfp1f3b7fjsn61c720e98696"
            },
            success: function (data) {

                const totalResults = data.totalResults;

                if (totalResults > 0) {

                    $.each(data.Search, function (i, item) {


                        const title = item.Title;
                        const poster = item.Poster;
                        const year = item.Year;


                        // Append our result into our page
                        $('#results').append('' +
                            '            <div class="shadow">\n' +
                            '<div class="card mb-3">\n' +
                            '                        <div class="row g-0 align-items-center">\n' +
                            '                            <div class="col-md-4">\n' +
                            `                                <img src="${poster}" class="card-img rounded p-1" alt="business-image">\n` +
                            '                            </div>\n' +
                            '                            <div class="col-md-8">\n' +
                            '                                <div class="card-body">\n' +
                            '                                    <div class="row">\n' +
                            '                                        <div class="col-md-9">\n' +
                            `                                            <h3 class="card-title">${title}</h3>\n` +
                            '                                        </div>\n' +
                            '                                        <div class="col-md-3">\n' +
                            `                                            <small class="text-muted">Year: ${year}</small>\n` +
                            '                                            <br>\n' +
                            `                                            <small class="fs-4 text-success fw-bold"></small>\n` +
                            '                                        </div>\n' +
                            '                                    </div>\n' +
                            '                                    </div class="row">\n' +
                            `                                    <a role="button" class="btn btn-primary" href="{% url 'review' %}">Read Your Reviews</a>\n` +
                            `                                    <a role="button" class="btn btn-primary" href="{% url 'review' %}">Write A New Review</a>\n` +
                            `                                      <div id="transaction-${i}"></div>\n` +
                            '                                </div>\n' +
                            '                            </div>\n' +
                            '                        </div>\n' +
                            '                    </div');
                    });
                } else {
                    // If our results are 0; no businesses were returned by the JSON therefore we display on the page no results were found
                    $('#results').append('<h5>No results were found!</h5>');
                }

            }
        });
    });


    function ratingGenerator(rating, index) {
        // 5-star rating generated via fa-star from fontAwesome
        for (let i = 0; i < 5; i++) {
            if (i < rating) {
                $('#rating-' + index).append('<span class="fa fa-star checked"></span>');
            } else {
                $('#rating-' + index).append('<span class="fa fa-star"></span>');
            }
        }
    }




});