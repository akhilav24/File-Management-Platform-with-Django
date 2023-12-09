<h1><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span style="font-size:24.999999999999996pt;">&nbsp;Installation and Setup</span></h1>
<p style="text-align: justify;"><span style="font-size:15pt;">Follow these steps to quickly set up and run the File management portal project on your system using Visual Studio Code and Django.&nbsp;</span></p>
<p><br></p>
<p style="text-align: justify;"><span style="font-size:15pt;">System Requirements&nbsp;</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">Before proceeding, ensure that you have the following installed:&nbsp;</span></p>
<ul>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Visual Studio Code:&nbsp;</span><a href="https://code.visualstudio.com/download"><u><span style="color:#1155cc;font-size:15pt;">Download and install Visual Studio Code from the official website.</span></u></a><span style="font-size:15pt;">&nbsp;</span></p>
    </li>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Python:&nbsp;</span><a href="https://www.python.org/downloads/"><u><span style="color:#1155cc;font-size:15pt;">Download and install Python from the official website.</span></u></a><span style="font-size:15pt;">&nbsp;</span></p>
    </li>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Git:&nbsp;</span><a href="https://github.com/git-guides/install-git"><u><span style="color:#1155cc;font-size:15pt;">Download and install Git from the official website.</span></u></a><span style="font-size:15pt;">&nbsp;</span></p>
    </li>
</ul>
<p><br></p>
<p style="text-align: justify;"><span style="font-size:15pt;">Installation Steps&nbsp;</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">1. Download the Project:&nbsp;</span></p>
<ul>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Open Visual Studio Code.&nbsp;</span></p>
    </li>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Use Git to clone the project repository:&nbsp;</span></p>
    </li>
</ul>
<p style="text-align: justify;"><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lsquo;git clone&nbsp;</span><a href="https://github.com/akhilav24/filesharing.git"><u><span style="color:#1155cc;font-size:15pt;">https://github.com/akhilav24/filesharing.git</span></u></a><span style="font-size:15pt;">&rsquo;</span></p>
<ul>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Alternatively, download and extract the project folder.&nbsp;</span></p>
    </li>
</ul>
<p style="text-align: justify;"><span style="font-size:15pt;">2. Install Required Packages:&nbsp;</span></p>
<ul>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Open the terminal in Visual Studio Code.&nbsp;</span></p>
    </li>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Navigate to the project directory using the cd [project_directory] command.&nbsp;</span></p>
    </li>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Install required packages using the following commands:&nbsp;</span></p>
    </li>
</ul>
<p style="text-align: justify;"><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &gt; pip install Django&nbsp;</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &gt; pip install django-bootstrap5&nbsp;</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &gt; pip install fontawesome_5&nbsp;</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">3. Enter Virtual Environment:&nbsp;</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &gt; pip install virtualenv</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &gt; virtualenv venv</span></p>
<h1><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></h1>
<ul>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Activate the virtual environment using the appropriate commands.</span></p>
    </li>
</ul>
<p style="text-align: justify;"><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Windows: &lsquo;venv\Scripts\activate&rsquo;</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Mac OS/ Linux: &lsquo;source/venv/bin/activate&rsquo;</span></p>
<p style="text-align: justify;"><span style="font-size:15pt;">4. Run the Server:&nbsp;</span></p>
<ul>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Execute the command &lsquo;python manage.py runserver&rsquo; in the terminal.&nbsp;</span></p>
    </li>
    <li style="list-style-type:disc;font-size:12pt;">
        <p style="text-align: justify;"><span style="font-size:15pt;">Open your web browser and go to &lsquo;http://localhost:8000/&rsquo; to access the portal.</span></p>
    </li>
</ul>

<h4>A brief documentation is shown in the link <a data-fr-linked="true" href="https://docs.google.com/document/d/1fFprqGQ0E261tNSEtP7RHZbwaOkrL1I1KiV2s8dcQVE/edit?usp=sharing">https://docs.google.com/document/d/1fFprqGQ0E261tNSEtP7RHZbwaOkrL1I1KiV2s8dcQVE/edit?usp=sharing</a></h4>


https://github.com/akhilav24/filesharing/assets/95332194/938bc68b-b83c-4a91-abe0-5b333916c863

