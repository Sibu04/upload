  const canvas = document.getElementById('myCanvas');
  const ctx = canvas.getContext('2d');
  const img = new Image();
  const zip = new JSZip();

  img.onload = function() {
    const fetchUrl = prompt('Please enter the fetch URL:');
    if (!fetchUrl) {
      console.error('Fetch URL is required');
      return;
    }

    fetch(fetchUrl)
      .then(response => response.json())
      .then(data => {
        const promises = [];
        data.forEach((item, index) => {
          console.log(`Loop ${index+1}`);
          
          // Parse time and call duration
          const startTime = item.time;
          const callDuration = item.call_duration;
          const startDateTime = new Date(`01/01/2022 ${startTime}`);
          
          // Updated code to calculate call duration in seconds
          const callDurationArr = callDuration.split(':');
          const hours = parseInt(callDurationArr[0]);
          const minutes = parseInt(callDurationArr[1]);
          const seconds = parseInt(callDurationArr[2]);
          const callDurationSec = hours * 3600 + minutes * 60 + seconds;
          
          const endDateTime = new Date(startDateTime.getTime() + callDurationSec * 1000);
          const formattedTime = `${format12Hours(endDateTime)}`;

          const textProps = [
            { text: formattedTime, x: 182, y: 76, color: 'white', size: '28px' },
            { text: item.Internet_speed + 'KB/s', x: 319, y: 76, color: 'white', size: '28px' },
            { text: item.call_duration, x: 440, y: 720, color: 'white', size: '60px' },
            { text: item.call_duration, x: 816, y: 1892, color: '#1E90FF', size: '30px' },
            { text: item.mobile_charge, x: 984, y: 74, color: 'WHITE', size: '26px' }
          ];

          function format12Hours(date) {
            let hours = date.getHours();
            const minutes = ('0' + date.getMinutes()).slice(-2);
            const amOrPm = hours >= 12 ? 'PM' : 'AM';
            hours = hours % 12;
            hours = hours ? hours : 12; // the hour '0' should be '12'
            return hours + ':' + minutes + ' ' + amOrPm;
          };

          // Draw the image and text on the canvas
          canvas.width = img.width;
          canvas.height = img.height;
          ctx.drawImage(img, 0, 0, img.width, img.height);

          textProps.forEach(props => {
            ctx.font = props.size + ' Arial';
            ctx.fillStyle = props.color;
            ctx.fillText(props.text, props.x, props.y);
          });

          const outputImg = new Image();
          outputImg.src = canvas.toDataURL();

          // Generate the screenshot filename
          const currentDate = new Date();
          const randomDate = new Date(Math.random() * (currentDate.getTime() - new Date('2021-01-01').getTime()) + new Date('2021-01-01').getTime());
          const dateFormatted = randomDate.toISOString().slice(0, 10);
          const time = formattedTime.replace(/\s(AM|PM)/i, '').replace(/:/g, '-');
          const milliseconds = Math.floor(Math.random() * 1000);
          const formattedMilliseconds = ("00" + milliseconds).slice(-3);
          const appName = Math.random() < 0.5 ? "com.android.incallui" : "lockscreen";
          const screenshotFilename = "Screenshot_" + dateFormatted + "-" + time.replace(/:/g, '-') + "-" + formattedMilliseconds + "_" + appName;

          // Create a download link for each output image
          const downloadLink = document.createElement('a');
          downloadLink.href = outputImg.src;
          downloadLink.download = screenshotFilename + '.png';
          downloadLink.textContent = 'Download';
          downloadLink.classList.add('download-link');
          document.getElementById('output-images-container').appendChild(downloadLink);

          promises.push(new Promise((resolve, reject) => {
            JSZipUtils.getBinaryContent(outputImg.src, (err, data) => {
              if (err) {
                console.error(`JSZipUtils Error: ${err}`);
                reject(err);
              } else {
                zip.file(screenshotFilename + '.png', data, { binary: true });
                resolve();
              }
            });
          }));
        });

        Promise.all(promises)
          .then(() => {
            zip.generateAsync({ type: 'blob' })
              .then(content => {
                saveAs(content, 'output-images.zip');
              });
          })
          .catch(err => {
            console.error(`Promise Error: ${err}`);
          });
      })
      .catch(err => {
        console.error(`Fetch Error: ${err.message}`);
      });
  };

  img.src = '../ss.png';

  document.getElementById('download-btn').addEventListener('click', () => {
    const downloadLinks = document.getElementsByClassName('download-link');
    if (downloadLinks.length === 0) {
      console.log('No images to download');
      return;
    }
    Array.from(downloadLinks).forEach(link => link.click());
  });