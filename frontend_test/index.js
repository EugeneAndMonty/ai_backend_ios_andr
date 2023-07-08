const test = async (e) =>   
await fetch(
    'http://fake-backend.chickenkiller.com:8000/for_test', 
    //'http://143.244.154.153:8000/for_test',

    //'https://1116-2601-2c6-4300-920-1c7b-e201-b6fa-99ad.ngrok-free.app/for_test',
    //'http://127.0.0.1:8000/for_test',
    {   
        method: 'POST',
        mode: 'no-cors',
        headers: {
        "Content-Type": "application/json; charset=UTF-8",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
      },
        body: JSON.stringify({data: true})
      })
      .then((resp) => {
        console.log(resp)
      });

document.getElementById('red').addEventListener('click', test)

