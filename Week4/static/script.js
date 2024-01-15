document.getElementById('submitBtn').addEventListener('click', function () {
  const pregnancies = document.getElementById('pregnancies').value;
  const glucose = document.getElementById('glucose').value;
  const insulin = document.getElementById('insulin').value;
  const bloodPressure = document.getElementById('blood_pressure').value;
  const skinThickness = document.getElementById('skin_thickness').value;
  const bmi = document.getElementById('bmi').value;
  const age = document.getElementById('age').value;
  const diabetesPedigree = document.getElementById('diabetesPedigree').value;

  const formData = {
    pregnancies,
    glucose,
    insulin,
    bloodPressure,
    skinThickness,
    bmi,
    age,
    diabetesPedigree,
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
