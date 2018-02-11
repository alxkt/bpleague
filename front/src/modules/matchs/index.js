import axios from 'axios';
import auth from '../auth';
import UIkit from 'uikit';

function addMatch(playerA, playerB, playerC, playerD, scoreAB, scoreCD) {
  const data = {
    playerA: playerA,
    playerB: playerB,
    playerC: playerC,
    playerD: playerD,
    scoreAB: scoreAB,
    scoreCD: scoreCD
  };

  return new Promise((resolve, reject) => {
    axios.put(process.env.API_URL + '/matchs', data)
      .then(function (response) {
        if (response.status === 200) {
          resolve();
        }
      })
      .catch(function (error) {
        if (error.response && error.response.status === 401) {
          auth.checkAuth().then(() => {
            addMatch(playerA, playerB, playerC, playerD, scoreAB, scoreCD).then(() => {
              resolve();
            }, () => {
              reject();
            });
          });
        } else {
          console.log(error);
          reject();
        }
      });
  });
}

export default {
  addMatch
}
