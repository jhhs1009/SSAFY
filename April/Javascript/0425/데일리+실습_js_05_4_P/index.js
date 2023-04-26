/* 
  아래에 코드를 작성해주세요.
*/

const input = document.querySelector('input')
const search = document.querySelector('button')

function fetchAlbums(page, limit) {
  page = 1
  limit = 10
  // alert('확인!')
  const keyword = document.getElementsByClassName('search-box__input')[0].value

  const baseurl = 'https://ws.audioscrobbler.com/2.0/?method=album.search&album='
  const api ='&api_key=ca6906a97e2c26b116562118b0593457&format=json'
  const URL = baseurl+keyword+api

  axios.get(URL)
  .then(function (response) {
    console.log(URL)

    const albums = response.data.results.albummatches.album
    
    const search_result = document.querySelector('.search-result')

    for (album in albums) {
      console.log(album)

      const search_result_card = document.createElement('div')
      search_result_card.classList.add('search-result__card')

      const image = document.createElement('img')
      image.src = albums[album].image[1]['#text']
      search_result_card.append(image)

      const text = document.createElement('div')
      text.classList.add('search-result__text')

      const name = document.createElement('h2')
      name.innerText = albums[album].artist
      text.append(name)

      const title = document.createElement('p')
      title.innerText = albums[album].name
      text.append(title)

      search_result_card.append(text)
      search_result.append(search_result_card)


    }
  })
  .catch((response) => {
    alert('잠시 후 다시 시도해주세요')
  })

  

  

}

search.addEventListener('click', fetchAlbums)



//ca6906a97e2c26b116562118b0593457