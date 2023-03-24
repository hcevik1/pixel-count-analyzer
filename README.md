
   <h1>Pixel-Count-Analyzer</h1>
    <p>Pixel-Count-Analyzer is a Python script that calculates the number of white pixels in images and saves the results in an Excel file.</p>
    <h2>Usage</h2>
    <h3>Running as a Python script</h3>
    <ol>
      <li>Clone the repository or download the <code>pixel-count-analyzer.py</code> file.</li>
      <li>Install the required packages by running the following command in your terminal:
        <pre><code>pip install openpyxl Pillow</code></pre>
      </li>
      <li>Place your images in a folder named <code>images</code> in the same directory as the <code>pixel_count_analyzer.py</code> file.</li>
      <li>Run the <code>pixel-count-analyzer.py</code> script by typing the following command in your terminal:
        <pre><code>python pixel-count-analyzer.py</code></pre>
      </li>
      <li>The script will create a folder named <code>output</code> and generate an Excel file in it with the results of the pixel count analysis. Each row in the Excel file represents an image and contains the filename, total pixel count, white pixel count, and percentage of white pixels.</li>
    </ol>
    <h3>Running as an executable file</h3>
    <ol>
      <li>Download the latest <code>pixel-count-analyzer.zip</code>release.</li>
      <li>Place your images in a folder named <code>images</code> in the same directory as the <code>pixel_count_analyzer.exe</code> file.</li>
      <li>Double-click the <code>pixel-count-analyzer.exe</code> file to run the script.</li>
      <li>The script will create a folder named <code>output</code> and generate an Excel file in it with the results of the pixel count analysis. Each row in the Excel file represents an image and contains the filename, total pixel count, white pixel count, and percentage of white pixels.</li>
    </ol>
    <h2>Supported Image Formats</h2>
    <p>The following image formats are supported: JPG, JPEG, PNG, BMP, TIFF, and TIF.</p>
    <h2>Requirements</h2>
    <ul>
      <li>Python 3.6 or later</li>
      <li><code>openpyxl</code> package</li>
      <li><code>Pillow</code> package</li>
    </ul>
    <h2>License</h2>
    <p>Pixel-Count-Analyzer is licensed under the MIT license. See <a href="LICENSE">LICENSE</a> for more information.</p>
