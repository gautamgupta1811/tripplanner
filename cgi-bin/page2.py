import cgi
import urllib.request as url
import bs4

form = cgi.FieldStorage()
tocity = form.getvalue('to')
tocity = tocity.lower()
fromcity = form.getvalue("from")
startdate = form.getvalue("start")
enddate = form.getvalue("end")
path = "https://www.msn.com/en-in/weather/today/" + tocity + "hindia/we-city?q=" + tocity
http = url.urlopen(path)
page = bs4.BeautifulSoup(http)
te = page.find('span', class_="current")
temp = te.text
info = page.find("div", class_="weather-info")
t = info.text
t = t.split("\n")

path2 = "https://www.goibibo.com/hotels/hotels-in-" + tocity
http2 = url.urlopen(path2)
page2 = bs4.BeautifulSoup(http2)
p = page2.find_all('a', class_="htl-name")

print("""
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://kit.fontawesome.com/9e8dabcc62.js"></script>
    <link rel="stylesheet" href="../CSS/style1.css">
    <link rel="stylesheet" media="screen and (max-width:768px)" href="../CSS/mobile.css">
    <link rel="stylesheet" media="screen and (min-width:1100px)" href="../CSS/widescreen.css">
    
    <title>Trip Planner </title>
    <style>
    .text-primary{
    color: #93cb52;
}
    a{
    text-decoration: none;
}

    #navbar{
    background: #333;
    color: #fff;
    position: sticky;
    top: 0;
    display: flex;
    justify-content: space-between;
    z-index: 1;
    padding: 1rem;
}
#navbar ul{
    display: flex;
    align-items: center;
    list-style: none;

}
#navbar ul li a{
    color: #fff;
    padding: 0.75rem;
    margin: 0 0.25rem;
}
#navbar ul li a:hover{
    background: #93cb52;
    border-radius: 5px;
}


    </style>
</head>
<body id="home">
    <nav id="navbar">
        <h1 class="logo">
            <span class="text-primary">
                <i class="fab fa-tripadvisor fa-2x"></i> TRIP
            </span> Planner
        </h1>
        <ul>
            <li><a href="#home">Weather</a></li>
            <li><a href="#what">Hotels</a></li>
            <li><a href="#who">Sights</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
""")
print("""
<header id="showcase">
        <div class="showcase-content">
            <h1 id="l-heading">
                CURRENT WEATHER IS : {}C""".format(temp))
for i in range(len(t)):
    print(t[i] + "<br>")

print("""                
            </h1>
            <!-- <form id="customize" action="https://google.com">
                <label for="1">FROM</label>
                <input type="text">
                <label for="2">TO</label>
                <input  type="text">
                <label for="3">START DATE</label>
                <input type="date">
                <label for="4">END DATE</label>
                <input type="date">
                <button type="submit" value="send" >SUBMIT</button>

            </form>
            <a href="#what" class="btn">Search</a> -->
        </div>
    </header>
    <section id="what" class="bg-light py-1">
            <div class="hotel-content">
                <h1 id="heading">
      
                    BEST HOTELS ARE :""")

for i in range(5):
    print(p[i].text + "<br>")

print("""
                </h1>
                    <!-- <h2 class="m-heading text-center">
                        <span class="text-primary">What</span> We plan
                    </h2>
                    <div class="items">
                        <div class="item">
                        <i class="fas fa-hotel fa-5x"></i>
                        <div class="ho">
                            <h3 class="ho">Hotels</h3>
                            <p>We recommend best Hotels according to your needs and which fits best in your budget ! </p>
                        </div>
                    </div>
                    <div class="item">
                        <i class="fas fa-plane-departure fa-5x"></i>
                            <div>
                                <h3>Transportation</h3>
                                <p>We'll take care of your transportation as well !!</p>
                           </div>
                     </div>
                     <div class="item">
                        <i class="fas fa-eye fa-5x"></i>
                            <div>
                                <h3>Sight seeing</h3>
                                <p>Cheers!! We will Plan everything for u.</p>
                           </div>
                     </div>
                 </div>    -->
                </div>


    </section>
    <section id="who">
        <!-- <div class="who-img"></div> -->
        <div class="">
             <h2 class="heading">
            BEST SIGHT SEEING SPOTS ARE  :     
            </h2>
<div class="row">            
            
    <div class="card" style="width: 18rem;">
          <img src="data:image/jpeg;base64,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" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Red Fort</h5>
            <p class="card-text">One of Delhi oldest moument.</p>
          </div>
          
          <div class="card-body">
            <a href="#" class="card-link">Visit</a>
            <a href="#" class="card-link">Means Of Transport</a>
          </div>
    </div>
    
    <div class="card" style="width: 18rem;">
           <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxQTEhUTExIVFhUWGBcXGBgYGBUWFxgWGBYXFxUZFxcYHiggGBolHRUYITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGzAlICY1LS0rLS0tLTcvLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIALcBEwMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAAEAAIDBQYBB//EAEQQAAIBAgQDBQUCDAUEAwEAAAECEQADBBIhMQVBUQYTImFxMoGRobEjQhQVM1JicoKywdHh8ENjosLxJFOS0hZzkwf/xAAbAQACAwEBAQAAAAAAAAAAAAADBAECBQYAB//EADIRAAICAQMCBAQFAwUAAAAAAAECAAMRBBIhMUEFE1FhMnGh8CIzscHhI4HRFEJSkfH/2gAMAwEAAhEDEQA/AKuwNQKusKlC4LDDQmra1brub7B0nI0VnqZ1Up5FOVaTClMxrEjo7hOHBdWYSAQY060Fl1qazegVV8lcCSmAcmb+3cDDyqayAKzPCeJj2dqvbd2sK2kocTXrsDDMOc1Az00XKExF+hKkITCRfqRMRVI+IrtvE0Q1SoeXxudKk7yq3DYmpjfoRSEDQrNUbNUPf0y5frwWezHXHFC3WFMuXaGuXKMqwZaSZtaOs3KphiV50RbxPSrMhkKwl1NZjjLEMWOsCrmzi6qe0IlcwO1Tpxh8GRacrMZi8cRcMbc6rr90lpmjcdYJl200AUbc6FsYbc9K6SoqBmc7d5jNj+8P4TxN0AUwV+nnV6MZ3oIRvXlVHw3h5uGJAFXnDOAlbjB/ZI0I5jrPL0pbUGoEk9Y5phbtA7Q/h7W1iIZuZPI1NjAA2Ytr/e1S2eFm17MnzPSj2wikaist7V3ZBmitZ24keH0WS2/WnPiNOUdZpuJwmm9VjAjQ+6aGqh+cyWJXiWeEvqFMnX50Lc4ioeJ0+lBZeW1RXrNGWpc8wZdscQrHcT/NOlUmOZmM5tPKiXs0JdSm6UVekC7M3WVL4bWlRpSlTvmGKeWIHg9hVjaqswbaVZWmqLesrUeJOBSy1zNSDUvDxrrTRUrmahIqwlSJJbQk6cq0/CBcCkvHl1qu4UFC6gUbiOIhV0NJXsXO0COUqEG4mHXL9BXbk1XjiS82roxyfnCgeSw7Qvmqe8IK1Jbt9aCPEU2zChcXxHKQ06TyqwqY8SptVRnM0XeqoEkCSAJ5k7D1rgxHWsrxLHC6qAayxPvA0/jUVtmH3nHvNYus8RGmuNTLnGO809PpDfWLFaarEY7LvUSY8GfKs1euuwgsSNND5EHf1FRtbOsfHSaXbxysEBaz/wB/+ww8Mc9W+k1bYio2uVlmtnq0ERzPLyNctIwPtN56kTOx39aqvjozzXx8/wCJY+FnHD/T+Zo7tsNTCMgBknkf51UWMfcAH3oOs7x5bfPpRmHx+aA8AQZPPy20rSp8X01hC5xn1H79IlZ4fcuTjPylnauzsafbLMSCJHKq6xdAOjSKLfE6SOVaHB+HmKcj4uJW8W4Y7MWK7bdKiHA1ygk+vKtFgsaSPFsN6h4iZAK0VdRYML0gjRWct1lM/C0QyDv0q94S1wIA3z3jlVG7uDz+FHcPvXJ1mrW7mXk5kV7VbgYmotPTiaDsXdNaIF0HnWaV5jwMbdUmq3FYY7HUf3tRt65HOgsTjo0o1QbtBPjvB/weOdQ4jTSm3cfNBXr8madRGPWLMyjpJbj0HdanG7Q125TKJAs0jY0qHZ9a7TO2L7hAcK9H23qrwrUYjUaxeYrS3EsFuU7PQS3aeLlLlIwHhBeud7UOems9e2yd0KGLI50LicYajZqGvmrKgzB2WNiQviTNRi83Wo2FPFM4EztzE9Y5LpB3qw703DoPUTQVtateF29SfT61l+K6saSg2gDPAGff+Jp+F6Y6i4Vk8dT9/OOw9gyJBAE7+kUf3PTf+tcKzpOXzOYc9tBXRYnZrZP66+72iOlfPdZqH1VxtYdcdPYYndaalaKhWD0guLuG2fGjFDqGVS8HYhgskesRyobD8UtgsLk2wSCocZSVygZjPsztB10q6w+HbmvwYHT3E1KltwTKGD1UjpQQgxyIUsc9ZXpetuPs3RhzIZWjQ9PdXHtmBIE+nP8AuOVT4nAW7h+1sIxGxKCY9aGbhFiRCMv6ty4nyDVG0GeyRHi2TI1EbbGR7/fSuWoIHUxrpyJ950pp4YoiLt/L/wDax66y2vzqPE8O1X7a6RMwSkgwYYMFmR6x1mvbBJ3GOuJtAHx/vpUuCfI0kaHSN+lQ2sKVbM90tEgDKqqJ5mN2/ntUhIOzCPcamtjU4de0q6h1Kt3l5mHpRFi8pGlU1tgxgtpRlsBToYiu6Kqw4OZywLA8iHmJqIkcqHu8RXaJqG5i1A6TUCtpJsWcvcRYEio7WPyzJ5UJjcYuvMxoapLl4k707XQGHIxE7dRsPXMvX4sxO9RPjCedU4uRS/CKZFKjoIudQT1MtO/phvVX99TTfq4rkedLA3agu3qDbEVBdxFEWuDa8Yk7XNaVV7XjSo2yLedEjxRAv0ArVIGoxAMBkjpDRfqRcTVfmruaqFBJFjCWnfV03KrBcqVL1DKQgv8AWGF6iuGmq9OFUxiW3boPkqRUqVVo21l5xXmsxIrpB7ytu4hUjMYnbQn6CrHhvGMOBBvIp55pX45hWa7bXgrWwkghWbwiTqQP9tUdq3eK5u8YggHUsAPnXG+N6lr3NJ+FSD75x/M6/wAH0i0oLf8AcQfljP8AE9Ws4+yfZv2T6XLf0zUUFzezB22IP0mvIgt0BpOY8iYMe7nvTF70AyqN6ov8F86wfIE2t5nsJw36J+BpqpBMSNORjr515PZ4heUezDToFa4o98MKLt9oMSonNeB6C7cP7xNR5HoZ7fPU8zcnb4t/Ok11+Z+KqfqK8yXtjiQAc1znoTac/wCq3RKduboALMDOsG0hI6zkK6140t2MjcPSeg5p0IU+4jn5EUy8umqAx+k0/Ez1rGjt4RGZLWvVbin/AEu0VOvblZhraSelxx+9bj51Xy3k5E1BVTyYc9GB/wBoqC/ZB+8w6+EH/d5VSr20s87bKfJ7TH5lTU6dqcO3K6v7Cn9xm61Q1v6SQw9YRctxuZHIwfnO3Oihfzc6AXjeHP8AiRP51u6v1SKkt8Tsf9+1qfzgD8DWt4JcaryjDAbv8ukz/FKvMqDDqP3mt4Vwq2UGcZi2s9PSuce4SCua0uo5DmP50Rw26pQFXV12BUgj4ijbV2TW0bnD7gZmipdm0iea4hjtQBuRXpPFMJZGa4ygkiDXmWJMsYGkmK2dJeLgcDEw9dSacHOZKtzrTGHOpMFgrlxgqqST9OvpWnwXYu4fbZQNNtSeu+1Ft1FdXxGCq09lw4EyebSozcra3+xhzQGGXnO8fSo8V2HMfZ3AdfvCNPUTrQ18Qo9YVvD7+wmLNyo2atTf7HXVB8SH0nXy1GlZu7hHzFcjZhuIJNNV6mt/hMWt01teNwgxNKmupBg6HoaVH3QOIwNUgam3VAPhMikizV94IzLESQNTgacMHcmO7edfuty35VHlMTBiYnlPT1qN4MqUI7R4NPU1EKetegyJOjUXZoK3R1qhPL1dZIBUhXSmqKmUUAmNqJgu1TZr5WJyhV2mJ166b1a4bh5yjwmI6N9areL4RzimZkbLn0bKYgRl8UenOvVeBLFi0I+4v0rgfEbG89ie5M7fQqBQoHoJg7XCy3s22P6oY/8AFOucLy6Mrr5HTX3ivQXxiI4VzlzezJgE9JPPf4GliMdb7xLUqzNrlBDQBzPT/mkBYTHNs86u4IBSRyBPImagto2UexI5+JfXevSeJYJDZu+BZyNGizMGINZ38U3VGttxA12Iq4fIlcTL3LRgAC2Tr98az5EUvwMkfkgdOqGrfEYgZQxgL1bYnmB1oO1jbWW4cwgrlnIQJ1gee9WzPYJ7QG9w8TPdMPcP4GgnwK7m2R7m/hWhwjoR4QrD9HQjpK1OcOpH8i386ndIImXwuHUSVBmCJgzJ5bTQ68PADHUExOm/XetnwbgPem5BiCvtSdwf5VYN2TYH8oo9Ax+VQbADPYM87TCZR4XjU+R+I1FaLsr2cvYm4FF8qiAF2kloMwADpmMHfb5VcYnsvcHssrT1lT86O7H4F8Ped3UaplBBU65geR6CjUbbbAvrBXMUQmbXB4FLFtbVsQijnqZOpJPMkmaYL8UNd4hIihGxI610KUkDGJiNaCcyzvuGEHnQSYK0hzaUDfxEc6r7uJJ0mjpS2ODAvco6iavDwGzKomN45VZpiDVFg74CiTrFOu8RA50m6kmNqwAl4b/nTHvdKz7cVHWmDjA61TyzLeYJdXGNctWVGpUT10+tUl3jQoS9x/zqwR5G9ZoXyTsKVY9uO670qv5TynmrAMJwJHCjNBnUjmP4VvuDcDsWPya+KACTqT8dqz+AAEQKvbF/w0TU6mx+M8SlGmrTkLzL1iI2qtv4e08gopDatoNTtJ6nahLGMymJ09a7duy2lLICph2wRMB2l4QMPdhCSjCVnfTcGqtRXouM4Urgm5r0HT31nrXAPEZMLJgc4610Gn16lMOeR9Zz2q8PfflBwfpKFBR1mtKvBLOWMpnrNQfiZQ4GbT51f/W1tKL4fanPEqFFEWlrVYjB23ti2sCNiOVTcM4HbTVvEfPb4Uq2vTbkjn0jq6F92AePWZDtBwh/wTvZAUMhjmRmj3akGrXumWyq2wpuBUXxDTSAZI1jerftjkGGOkKro7R+ahzt+7HvrH//ACpvD/0t7XXaNIneuR8Wta24N7TpvDqlrqI95Y4jAXby5by2TrIguPgY0pmD4U2H8VqwhJ0/KEmN9MyQNutDJ2pn2rN4fGnW+2FsbpdHqo6etZmGmhLVcQz2buZcrKGUiQY8M7jyIPvoDthxZbdps05EAZgu7EmLdv0JGvkKFv8AabDEXQCyM4J1BEkoADpI5CqbimKt8QyWkzoWfOcyBgQEjWGEAb0SqtmcKB1lHYKpJmExvGLl1izA+QEaDoo5CoUx8/yO/wAK2WM7F3FU5GtuehGU+6ZH0rKYzhpEhlKsuhU6EH3/APBrRsoarh1xFq71s+BswjB4oqwZCVK66b+vnXo3ZPiy3gWZVzCO9WAQZ2uKDtr7VeQ2rzKdTqNj1rY9jsXlxNtswVWBDEmBlKzHxA+FLXV4GYZHzPVUtKreEKNNcoy/GImq/iuJaM9ooXQ+yTGYbMPWJ98dKlw2PtscqXVcga5SCYnnBqG3w+xOYWULS0kqsySZ199I7vWGxA8HxK/duqGtGyigli0nMeQBgRvVm76xQ9/hNgg/ZIPQKD8Vg03DWO7UoPZB8OpOhAJ313mmdG4GprPuP1i+pXNL/I/pHXHoW5cqcgnYUvxfcZioQyP732ru8qOs5Ahj0gF27QrXKv8AhHDQzkOCCp25e+rHi/DBcUAQsHQgfLShtqkRtssuld13fSZNcWdpNSsWiaYMGVYhxt8Klc8hUWFc8S1QbH4oDcvsNKh741NcMUDec1GRL4I7x1y951Az9TQ9xjUDXDUSRCi4pUAXNKozJm1w3EQFBnWj7fFZGgrFJcNFWcSRzoBpBhRcRNbbx4G9G2MaKx9u9NWFjERUGmeF00oxObQVx/pVVYvg0bbfzqu3bL7t0JW8BTHug0NcptuiqB1gmY9JZ4R+QFWNvNzoTAnKPWpy086A5yYdBgSr7X2i9gW1M95cRSP0JzXD/wCIPxoLJptGnWudsMctjubrFom4kLGudNDr0I+ZqhsdsbJbLlcQJ1Xf3Amub8SDNdwOk29DgV5mnRwdmHyn609YjSffNUQ7RYUxOSf1PrIp/wCPMH/l+9VH1pHbjtG4Rcw4LYhjlMoFAI6WyZn9r5U3s9wdbaBwGDMi5gY06xp1oe/2hwgDL3oAcaQJiFCfdmNh0rTdm7yOoYagoIkET7jT2hcpcp++kV1abqmErblqsz2z4WHsm6B47Yknqn3gese0PQ9a9HOCRSW38jyrL9rsMzWri2WCMVMyJBEeJfKRInlXT2WLahXHaYFaNU4YHvPFcRhwXkmFHPmeoAq44Fhxce0o0BYKPKTBnrVTjbQ0PlWz/wD57ZGrQCVKgHpqZjpXO2thMzfQfil5gex6pcJdpUrACkqZnc1J/wDFLMQGuSDuG13O9aLEXlUjM6jfcgfCh2ZW1W6AJ5FSPnWaXb1jIUSiPZlVBi9eH7Q+WmlQrwd1voi4m9BAOpkHxQR5bj51f5TsLo/0UM9oqwOcHfy6EQJ9astrKwOZDICCJtMHZW2oEDzI5nqaVy50qgTGkRrNFNjwRNdc9LZz1nNrauMdIcxA150Dib5nf3VBdxw60DexdeWpp5rVjsQpYHqaCfhjbhhFTjF118QKuS68CVG1oGeHwJmg8VggdqsLuK0gUFcvV4F5OFlTewZoG/YIq8aWofE2QBrVhZjrINYI4lAaVWsJ+aKVT53tB+SfWd75YjQVwqpiDQCXPKirN3yqE46Sz4PWGJbETNS2nqFG0qfD25NHV+OYuyc8Qyzco6xcPKlhEAA8OtG4dhyFAa4ekOtB7mOWwx3NOTwmnG9SEGqhz3lygHSEreqQXaGC9DUttPOoOJ4AzMdr8Qt2/h8NBLZhcmRAGsyPRTU68GtBswUgwR90DX0WjuKYVTiLd0AZgpXYees/L3mngmdq5bxFz55A++BOg0SjyR994I3Cbcicw9Cp/wBtcTg1sn7w94/lVhGuoHw/pT7ciZC+7/ilMkxkDEzp4CrYkiBlFpdTqZLvG3kKtOwmK+wAG6yseQMj5EVOjnvm29i36e1dqLsiipaXKNWUMx11Jp3RnNyj76GLaoYqaaN77EVV8QaUYdVb6GjHuTQt/YjyrpQMTBJzPDb+wPlWw7AH7Fz/AJh+QB/jWPu+yPhWs7Dn7Bh0uN+6tc9f+XN2v45pu0PARiLiN+iynWOYK7e+gcP2TCKQGO5iGfbQxpHnWrIAiP70prg6wJNIB26RkgTLDsuTrnYeRe4KB4n2aYKozmGdQfG7emh5aVrmDHy+dR3xoAQdwetWDsDI2jE5wfAd3bS2BsBMdTuas7vD42bTnUVi7AEVIcR5111djmtSPQfpOaetd7Z9TEmEUDxCfjQ2IwaQYny12qRrxoZ2qQXznMjamMYgFxIqFzRj1DcblE0bfB7AIMAZplxq6SaFxOKCnU84JkeGRIza6Tp8aq3HJkqYmumqfj2NuoPAs8yx1CgEaEedM4jx5cxt2zrDAvpAIAOmuv8AWs9juLG4pssdJBBkhjpIBOxpG/UoMgfSMpWepkWI43fViM8+YVI1E6Ss86VV9wNOjxtprpp6UqS81vX6mG2j0m1XaicO0bRXn74pyCHckHU6/DQn6VJheJXLQIVyAwkHy6xy3p0ar2gPK956QjeUUTZMaisjwTtCSMt3XL94e1z3k61fvxiyLecMTGwAOZjMAD3mjrqazwTg+kG1bdZeJiDUtu61Za32qtR4rdxT0gHTmdDtWis3pAI2IBHodRVksR/hkMCOssLd6iLd7rVcj0TaaiYErkw9blSB6GWnqarJ5nMWfEn7X0riE8tahxT+NIiYY6nloCaksljMZdvOuU8Q51LffYTotF+Sv33k7NtXJb389NKgFtgYke+aeEfqP9VK/OMfKcw8982v3LfkPauVzs2R3Nv9QV0ORcI8M5E6/nPTMBeVLCkkKoXUkwAJjc05o/zlz6xfVflNLi4BG9Cs1DYbH27hIS4rEcgwJ+VMx+NW0FzEAO2UEmBmIOUe+IrphyOOZg459J4/iUhFPPPcU/si2R+8a1XYpQLB8ySfWSv0UVm8Xbmxn5C/cXbaUtka9fCfhWk7Ex+D/tMI9IP+6sHUD+mZtU/EJvbbbHWTG/pT95FRrc8C5QOVJnefugRzms2NxjrGnXppUN1fDv08+Yqdi5G6/A/zqNlbKdV26f1qZ6SWfZFMY1leP425avIytHgB0nKYY7jWdKZhe1GezdBb7RVZgYA25DqdDW7pNeuwIR0H6TB1NJFhPvDO1PFFtqFzePUwDHLQtG/pWXXibtDMzggbg7CQNp03+tQ8YxputmPtZQCywNRsx5cx02qixOIIUyZAPtAz5R5f1FK2Wm59w/t/MsowMTdp2lRbTMMzEZRlIgLOgJYT4T9R51nR2iutcLi4QdoHQbyuw2mfM1SW8VmGVdDyM6AAaa8tfrVwMIq4cuR4dRAjvDyzNlPsEjT12q76izaATjEgIMw+x2ocW3VoY8n10mem/lttWefGAyxPqZ3M1Mtq0UBRLjGAY08IbQE5euuv0oW5hFIMabCNDofQbedANps4cniWC46SNsQJzBoManXNr/x8qr72MYsp6RHIf033o7EIDa8OrrGsAlgpgRE6a/Oqe5c1ke6mKlBnukKGLnUhZ9/8DSoHKOtKi7BPZkvespPxPkdpmpsJb5tqWIiSNuZnrMaGgkYjUGKmAGZYJOx1ogHMqekJW+A2k5TM7+119aOwXEcr6+z5iSTzquwOQ6XCwXkQNj1ogYwnM5VYiNBrAgAx7t6BaAxIxLASwx4JIZCGjwkcguvT3fKrRu0V8IFchIH3faKiBqRv7qz5xwzMQYVpExEbHSNqZ3yRqSVAyjmf72+FVTeBjMqQJusL2uiwHKF3GkiFU9DqZGnlvWuweJDqrqfCwBGkaHbQ14zh8RHhIJRgSAOR5egrRdnO0Zw65TDISDEwVkicoHLy605Ve44fp2g2rHaeoo9Shqz+E45bdGZbinQwPZO5gENsYiqTtH2za1dVLOVgBLcySTsNfL3zTLWqIMVt6TW4/iVu26hpLEHwqpdvUhdQKFtcaWT9nf5f4T+flUGF4jayrecqhZFzFoVzpIDbedH4fH2jMXA36sN9DpXMap1a5iOeZvabisDMIt44ESLV7X/LYeWxrj49V17q9/8Amx+VPTGpyuD4f1rlviNttroMb+XlvS/EY3SD8cLnH2V6SD/hPOh6dNao+1xnAgiQDeO8gjxXCAVPMaaGrjGcRspcS410KMrrtE5ip3n9Gs32pxJbBObTC5F8t4SCcrFmJgEwRm+VHqwWGIC4/gaUPAGctI8Pd7kEgyRoZ2O/9irvFccFy0wujMbd22VBkDNlukTO48NZrB8Te3byvbuKNTIBCwdBrGnLfz1qW/iy2HcKjHK9owVac0XQwOkgz6UwEtFhxkD2mWGUrkGOGKH4JcUg+O/I6AgA6+6R76vOwbTZYf5jfupWTW6PwdgTEXU+aXP/AFrS9hcSotPmYAZ21J/Rt0fUD+mY7QcuJvr2Jy20IVnMqITf11IoX8YvmgYW9sNzb/8Aag8N2htsFUBmuS4FtAWc5GIkKoJIIE+lMtdsMOXK+KQs7FdjBA8OpB0rNCnuI27qpwTgy2OLuR+QOv6SA/Imo72LvCALEg8xcTT41Xr2mtFsmS4GkAA8yZyiQNyBMb9YNDP2qOYgYe6QqFmU6OrKpaIjX7o99EFT5I2n6yhtT/kJX9qbxa3bL28g8QBLqQZiJK7bVjr1uHEjRgQdTHl/fnWl7dXctpEc2wGbvLbI7MAJWUeR7WVydOgjnVMnAbiWluliA6d5bB7wB9dcsgA6H6daaTTWLnIx7TPvIZsjvKvF3IXKLiZSCCARow5ETv50Bh73gIKZpMTJA5HU9dBV9guxt/ENdI0t2yJu+AiWAaCsgsYYTExBmmWOBgMU74HK+XNHh0n7oJOon30ytZXC9zAFgASe0p7No5pUHUgxr10E77c6twSxCMsHZvzQDtqPKiH7LXVJVGUnKGB5MGkplIJ3Ck8ooDEcNuW3upIBtqGJE7HUT19AP4VWypm5kya5eS06hCxmAwMZdAdNNiJ+VRvfRQY5aEb+EdQenrG9dfgWISC9tgxcajLGYkKupbUFmAJG1VlzAEDPLe0AVCnQgAsM22gP9xVRpvUycxYC8VMiQJ3302ihHw+pJYbny56x6dKOx+Cy3DuJhwARPdtsw5aHTUz9a5hOGsZY22a2oJknLIDQSBGvp60ZV7jvKk84lRctwSBr59a7V+Utf9n5A/xrtHkZ9o1OGWSBmdFLAeGPEGIOklgZkLyG7dBMmHw823yWhAKpqM2Y5gMwKmJ1OxOvwpYbD2+/tnIVEgSwYDPrJ8WnSthxTGWVvCy9kZFW2FYAAZtTBgaGTz3oTHAyO0MFz17zO/i0RbUW0DlGuFittQWAlbYRgCdSJJ2nlUiYUkqrfg0Oc9wDus2cFsqgKNogRt4z7rLB2rbXpGHGWWZMwXw+EBsxGY7gEaDnWjR0GgEemn0pZrMHiHFYImLwnCAAoayjBnXOFS80KMsspC+1Juaa6QPOpk4IMs92mcskg2CVCgFXiRzkNtyiteXG+h+JrouDoPnXjZme24lJ+JrBuSUKITAZLSrlEiZyjMpIkSBGtM4vasnEhLFiwLRQad2vdm6M2bKW1Y5RMRymiO1uLZMLcNswxygRIOrqND11rH8FxSrcsNed863CImTnzQcxO3IfteVErUbCZGMnH32E2XB+AX1JY2gLRQF3AtAtCMAF8U+2x5SYHSg7OOOEfMbCXjdLWjKiRoozMxBAGraACY3rWdmHF7Fdy4V1tA3XB8QdyYQMDICrMhddQKivYu1cuNbIKkOSFIKk5H0Kx7QkDbymruPLCuJC4JIxPPsQQbirlV86fn3FIgsBABB2A3GlPsWoXKtke5sQSfQacq9ICLmzwM350HN8d6lF3z+bUiVB4lvLWeci2xKyiSVclQ9wBSpAXXMCTqf5GpH4mL/2otIg9kAC4NF8IP2YUNMc9dulb67ZRmDsqlxsxnMv6rbj3U7DgW1yrIGsDM3MyefU17b+Ej1xJNaE5nn2HwbXHWbeZJ1yriGIPM+E7QOfWieIYZrSl0sm2CDDMlxXzLDKFLGBzPurfi+353zao8QucQ6ow3GbUdOfrUqoEkIg6Tziz2SxLnvFHeW3UMJIA8UHQMdRzmOdWeG7MXgro1phmKmVEjSfTXWtrwjEo2It2A6yCJRZOVVBIBA0UeGNYojtXxNLeJyMwQsqkSAFY7aHadBR8OUzLK9afhxPOz2EuFWXLch3V9lWCocQJ0/xPlR2H7LXLFqMuVFJdnZlJ2AMhZ00Far8J6sD7qX4UOX8KExZhgmEFiDkLM/2c4S9pbOIQSxt+JXKqp1KgEhc4EgnQ9Kosd3tjEKoZi3dveQZxlyhWOUACQfCSG3Nbdrw18O++g1PnQWJwlt3ztblsuScxHh8QjQ7eJvjRUfaQR99P8QFgFmS3Oev38uJQYTD3sQ4usyJme6mUuXKugZTLAcwpEjcVTPxK+b6YjuiDceMqyiuCIgMcxCaD51vbbBRAWNWbedWJLEepJ+NRG2sAZBCmVHQ9R03orahmJLd/wDJP7wS1IqhVGPsD9pjXS9jLVq5dNtVt3Vspb7syqEZQDpDe0oPPw1Y4fD3e5fB99ba0LbXEHdn8pADZTIyD7Qe/WBWgtWlWcqASSTA3JMknzJpFR0A9AJqTqGI/vmSEAOcTMdmuN3ktWu8UOl/wBmdj3QDd3nCHnDKAZ9aMvdmlNwt3ikHNJKw3imdmyk6jWOXKj7GFRLa2goIXRSwVmA6ajb1FaXsjZtubjOiuPZhtYMSdOR1FeJNjDHbP+ZXoORMrg+HBGukusOzEKqgABhDACIUbmB191RXOHr3rXMxOYBW2kqAInSJkb9KMx1wLcdRBCsy7zEHY+dBviP71ofMuTHvbSWbKxZipYzqSpBUnTlA+FAX8Fa1+zbXeSuvrpT7l+hruIqdsjdOXrSGJDeEQstOUdBpoKGZlXRWcDoGgfCKbcxNCXb9WCypaPOTq3xX+VdoI3qVW2iRuMvOA27Fy8uZmY5ZIIOUCMrZeskjU8m9aPVrV17haZLHfUZcwEER0zfDnSpUNzis/feGAy4iTCKuxYryBOwkbNEg6tpqNBFSpj8OpVbj3EJjQjPrrMEToNN6VKlkbccGGYYEs7FtCAQxO3KOsn09nz3p2JZkUHKDG5zEACBqBBPMj9nzpUqW81s4h/KWUmPxTYjLbtWswFxGc5wBCHNl8QB1YDkdKqLvY+/duO9wqgd2bwnNEkncxygaDXypUqI+peo7VgloVxkz0zsjwsK7XGGUgJ7J0MZt9BpEaeVVhwouqZQFcx3MEGZkQJB8xSpVey5zQH7zy1L5hXtI7eDxK/k2W4v5txvEPS4BJ94J86jxvGhY/Lo9udAfC4PplYn4gUqVApuaxwplra1Rdwk+F4ulxQysYOwIINMxHHLSe0xHuY/SlSowyX2zxRdm6KxxFrgmzZZuhZkRfjJYf+NP/Ar1z8s7AfmWoUehuTmPqMtdpUvZqGViBJrpVlBMuOzfD07zu1UoMr7ZRuIJkc9d6l7U2170BtV7tRr4pid+tKlTlbk6dn7wDoBaF7TOJwxBJsXWtRErGa3rEeBthqPZIp1zEXLY8dtXAjW20GDMHJcgDY/eNKlQBcx6whqUdIyxx/Ds2TOQ35pVp+IBHzqzRQwkailSphxt6QSDcMzpw5PShMU2SSzAAeRP0pUqqpyZO2Ut3tFazZVYs3RVI6AatA504XMVcHgtKgPO44J8jlSZ+IpUqPZ+AcQAJLERj8Guv+VvM3VUi2vyOY/+VaPs29vCWwCoUPdCjKPvEASevrXKVUS1pZkEoe1XDf8AqbrW2yNmJkbGQJzL97b3VS2sUS3duuW5EwDKkdQf5xSpUYnkiUMnew3T5ig7oPSlSqisTJIgd2aEuNSpUUGDMGJpUqVWkT//2Q==" >
          <div class="card-body">
            <h5 class="card-title">India Gate</h5>
            <p class="card-text">The India Gate is located at the heart of India’s capital city, New Delhi.</p>
          </div>
          
          <div class="card-body">
            <a href="#" class="card-link">Visit</a>
            <a href="#" class="card-link">Means of Transport</a>
          </div>
    </div>
</div>    
                 <!-- <p>We are a team of passionate learning Engineers.</p>
                 <h3>Our Team</h3>
             <ul class="list">
                <li>Gautam Gupta  </li>
                <li>Shaleen Govil </li>
                <li>Sumit Kumar</li>
                <li>Ujjwal Kumar</li>
                
            </ul> -->
        </div>
    </section>
    <!-- <section id="clients" class="py-1">
        <div class="container">
            <h2 class="m-heading text-center">
                <span class="text-primary">Our</span>
                Clients
            </h2>
            <div class="things py-1">
                <div><img src="./logos/logo1.png" alt=""></div>
                <div><img src="./logos/logo2.png" alt=""></div>
                <div><img src="./logos/logo3.png" alt=""></div>
                <div><img src="./logos/logo4.png" alt=""></div>
                <div><img src="./logos/logo5.png" alt=""></div>
            </div>
        </div> -->

    </section>
    <section id="contact">
        <div class="contact-form bg-primary p-2">
            <h2 class="m-heading">Contact Us</h2>
            <p>please use the form below to contact us</p>
            <form action="https://formspree.io/shaleengovil2000@gmail.com" method="POST" target="_blank">
                <div class="group"> 
                    <label for="1">Name</label>
                    <input type="text" name="name" placeholder="Enter name">
                </div>
                <div class="group">
                    <label for="2">E-mail</label>
                    <input type="email" name="_replyto" placeholder="Enter Email">
                </div>
                <div class="group">
                    <label for="3">Phone Number</label>
                    <input type="number" name="Number" placeholder="Enter Number">
                </div>

                <div class="group">
                    <label for="1">Name</label>
                    <input type="message" name="Message" placeholder="Enter Message">
                </div>
                <input type="submit" value="Send" class="btn btn-dark">
            </form>

        </div>
        <div class="map">
            <h1 class="heading"> 
                CHAT WITH US
            </h1>
            <a href="#">Chat</a>
        </div>
    </section>
    <footer id="main-footer" class="bg-dark text-center">
        <div class="container">
                <p>Copyright &copy; 2019 Logic Loaders,&nbsp; All Rights Reserved</p>

        </div>
        
    </footer>

    <!-- <script
  src="https://code.jquery.com/jquery-3.4.1.min.js"
  integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
  crossorigin="anonymous"></script>

  
    <script src="js/main.js" type=""></script>
   
    <script src="https://maps.googleapis.com/""")

print("""
</body>
</html>
""")
