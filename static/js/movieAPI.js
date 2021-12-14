$(document).ready(function () {

    $('button').click(function () {
        let title;
        let poster;
        let year;

        // Clear before adding in case the user clicks the button twice
        $('#results').empty();

        // Get the search
        const movie_title = $('input[name=movie_title]').val();


        $.ajax({
            "async": true,
            "crossDomain": true,
            "data": {'s': movie_title, 'r': 'json', 'page': '1'},
            "url": "https://movie-database-imdb-alternative.p.rapidapi.com/",
            "method": "GET",
            "headers": {
                "x-rapidapi-host": "movie-database-imdb-alternative.p.rapidapi.com",
                "x-rapidapi-key": "#"
            },
            success: function (data) {

                const totalResults = data.totalResults;


                if (totalResults > 0) {

                    $.each(data.Search, function (i, item) {


                        title = item.Title;
                        poster = item.Poster;
                        year = item.Year;


                        // Append result
                        $('#results').append('' +
                            '            <div class="shadow">\n' +
                            '<div class="card mb-3">\n' +
                            '                        <div class="row g-0 align-items-center">\n' +
                            '                            <div class="col-md-4">\n' +
                            `                                <img src="${poster}" class="card-img rounded p-1" id="movie-poster-${i}" alt="movie-poster">\n` +
                            '                            </div>\n' +
                            '                            <div class="col-md-8">\n' +
                            '                                <div class="card-body">\n' +
                            '                                    <div class="row">\n' +
                            '                                        <div class="col-md-9">\n' +
                            `                                            <h3 class="card-title" id="movie-title-${i}">${title}</h3>\n` +
                            '                                        </div>\n' +
                            '                                        <div class="col-md-3">\n' +
                            `                                            <small class="text-muted" id="movie-year-${i}">Year: ${year}</small>\n` +
                            '                                            <br>\n' +
                            `                                            <small class="fs-4 text-success fw-bold"></small>\n` +
                            '                                        </div>\n' +
                            '                                    </div>\n' +
                            '                                    </div class="row">\n' +
                            `                                    <button onclick="foo(${i})" class="btn btn-primary" id="write-review">Write Review</button>\n` +
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
});

function foo(i) {
    title = $('#movie-title-' + i).text();
    poster = $('#movie-poster-' + i).attr("src");
    year = $('#movie-year-' + i).text();

    $('#title').val(title);
    $('#image').val(poster);
    $('#year').val(year);
    $('#movie-form').submit();
}
