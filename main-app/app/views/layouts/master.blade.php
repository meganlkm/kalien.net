<!DOCTYPE html>
<html lang="en">

    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="kalien.net is awesome">
        <meta name="author" content="megan@devstuff.io">

        <title>kalien.net</title>

        <!-- css -->
        {{ HTML::style('assets/fonts/font-awesome/css/font-awesome.min.css') }}
        {{ HTML::style('assets/css/bootstrap.min.css') }}
        {{ HTML::style('assets/css/kalien.css') }}

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

    </head>

    <body>

        @include('sections.nav')

        @yield('content')

        <footer class='navbar-fixed-bottom centered'>
            <div class="container">
                <p class="copyright text-muted small">kalien.net is awesome</p>
            </div>
        </footer>

        <!-- js -->
        {{ HTML::script('assets/js/jquery.js') }}
        {{ HTML::script('assets/js/bootstrap.min.js') }}
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
            ga('create', 'UA-2917966-1', 'auto');
            ga('send', 'pageview');
        </script>
    </body>
</html>
