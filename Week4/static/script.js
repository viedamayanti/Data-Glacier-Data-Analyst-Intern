document.getElementById('submitBtn').addEventListener('click', function () {
  const glucose = document.getElementById('glucose').value;
  const insulin = document.getElementById('insulin').value;
  const bmi = document.getElementById('bmi').value;
  const age = document.getElementById('age').value;

  const formData = {
    glucose,
    insulin,
    bmi,
    age,
  };

  console.log(formData);

  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((prediction) => {
      console.log('Received prediction:', prediction);
      document.getElementById(
        'predictionResult'
      ).innerText = `Predicted: ${prediction_text}`;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
