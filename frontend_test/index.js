

const test = async (e) =>   
await fetch(
    'https://143.244.154.153:8000/for_test', 
    {   
        method: 'post',
        mode: 'cors',
        headers: {"Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",

      },
        body: JSON.stringify(
          true
        )
      })
      .then((resp) => {
        console.log(resp.json())
      });

document.getElementById('red').addEventListener('click', test)

