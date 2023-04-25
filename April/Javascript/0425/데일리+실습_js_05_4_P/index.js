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
  console.log(keyword)

  const baseurl = 'https://ws.audioscrobbler.com/2.0/?method=album.search&album='
  const api ='&api_key=ca6906a97e2c26b116562118b0593457&format=json'
  const URL = baseurl+keyword+api

  axios.get(URL)
  .then(function (response) {
    console.log(URL)
  })

}

search.addEventListener('click', fetchAlbums)



//ca6906a97e2c26b116562118b0593457