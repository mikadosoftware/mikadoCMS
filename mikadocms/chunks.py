HDR="""<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset='utf-8' />
    <!-- %meta{:content => "IE=edge,chrome=1", "http-equiv" => "X-UA-Compatible"} -->
    <title></title>
    <meta content='MikadoSoftware | continuous integration and delivery' name='description' />
    <meta content='width=device-width' name='viewport' />
    <!--[if lt IE 9]>
      <script src='http://html5shim.googlecode.com/svn/trunk/html5.js'></script>
    <![endif]-->
    <link href='/static/favicon.ico' rel='shortcut icon' />
<link href='/static/images/apple-touch-icon-144-precomposed.png' rel='apple-touch-icon-precomposed' sizes='144x144' />
<link href='/static/images/apple-touch-icon-114-precomposed.png' rel='apple-touch-icon-precomposed' sizes='114x114' />
<link href='/static/images/apple-touch-icon-72-precomposed.png' rel='apple-touch-icon-precomposed' sizes='72x72' />
<link href='/static/images/apple-touch-icon-57-precomposed.png' rel='apple-touch-icon-precomposed' />

<!-- STYLESHEETS -->
    <link href="/static/stylesheets/bootstrap.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/static/stylesheets/responsive.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/static/stylesheets/font-awesome.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/static/stylesheets/theme.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/static/stylesheets/fonts.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/static/stylesheets/mikado.css" media="screen" rel="stylesheet" type="text/css" />
  </head>
"""

TOPPAGE="""
    <!-- Page Header -->

      <nav class='navbar'>
        <div class='navbar-inner'>
          <div class='container'>
            <h1 class='brand'>
              <a href='/'>
                <img src="/static/images/mikado_logo_trans_small.png" />
              </a>
            </h1>
<!--           <form class="navbar-form pull-right">
            <input type="text" class="span2">
            <button type="submit" class="btn">Submit</button>
           </form> -->
            <div class='nav-collapse'>
              <ul class='nav pull-right'>
                <li class=''><a href="#">Open Source Software for Complex Businesses.</a></li>
              </ul>

            </div>
          </div>
        </div>
      </nav>

"""



FOOTER="""
    <!-- Page Footer -->
    <footer class='section' id='footer' role='contentinfo'>
      <div class='container'>
        <div class='row-fluid'>

           <div class='span4'>
            <h3 id="contactme">Contact me</h3>
            <p>
            &nbsp;
            </p>
            <ul class='icons'>
              <li>
                <i class='icon-envelope'></i>
                <a href='mailto:paul@mikadosoftware.com'>Paul Brian</a>
              </li>

              <li>
                <i class='icon-phone'></i>
                <a>07540 456 115 / 0207 617 7971</a>
              </li>

              <li>
                <i class='icon-twitter'></i>
                <a>@lifeisstillgood</a>
              </li>

            </ul>
          </div>

                </h4>
              </li>
            </ul>
          </div>

        <div class="span4">
License:
   <a rel="license"
   href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB">
   <img alt="Creative Commons Licence"
        style="border-width:0"
        src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" />
   </a>
        </div>
        </div>
      </div>



    </footer>
  </body>
  <script src="/static/javascripts/jquery.min.js" type="text/javascript"></script>
  <script src="/static/javascripts/bootstrap.js" type="text/javascript"></script>
  <script src="/static/javascripts/script.js" type="text/javascript"></script>
  <!-- Asynchronous Google Analytics snippet. Change UA-XXXXX-X to be your site's ID. mathiasbynens.be/notes/async-analytics-snippet -->
  <script type='text/javascript'>
    //<![CDATA[
      var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
      (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
      g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
      s.parentNode.insertBefore(g,s)}(document,'script'));
    //]]>
  </script>
</html>
"""

allchunks={'HDR':HDR 
           ,'FOOTER':FOOTER 
           ,'TOPPAGE':TOPPAGE

          }
