### Step-by-Step Guide: Deploying a Streamlit App on AWS EC2 using VSC

This blog post provides a detailed, step-by-step guide for deploying the "Technical Analyst Stock Markets" Streamlit app on an AWS EC2 instance using Visual Studio Code (VSC). This deployment approach ensures that your application is production-ready, scalable, and secure.

#### Prerequisites

Before proceeding, ensure you have the following:

1. **AWS Account**: Access to an AWS account.
2. **EC2 Instance**: A running EC2 instance with proper security groups allowing inbound traffic on port 8080.
3. **SSH Key**: SSH key pair for accessing the EC2 instance.
4. **Visual Studio Code (VSC)**: Installed locally with the Remote - SSH extension.
5. **GitHub Repository**: Clone the repository [Technical Analyst Stock Markets](https://github.com/vanhoangkha/Technical-Analyst-Stock-Markets.git).

### Step 1: Launch an EC2 Instance

1. **Login to AWS Console**: Navigate to the EC2 Dashboard.
2. **Launch Instance**:
   - Choose an Amazon Machine Image (AMI). For this guide, select **Ubuntu Server 22.04 LTS**.
   - Choose an instance type (e.g., **t2.micro** for testing or **t3.medium** for better performance).
   - Configure instance details. Set the **Auto-assign Public IP** to **Enable**.
   - Add storage (default settings are usually sufficient).
   - Configure security groups. Ensure to allow inbound traffic on **port 22** (SSH) and **port 8080** (Streamlit).
   - Launch the instance using your SSH key pair.

### Step 2: Access EC2 Instance via Visual Studio Code

1. **Install the Remote - SSH Extension**:
   - Open VSC and navigate to the Extensions view by clicking on the square icon in the sidebar.
   - Search for "Remote - SSH" and install it.

2. **Connect to the EC2 Instance**:
   - Press `Ctrl + Shift + P` and type "Remote-SSH: Connect to Host...".
   - Enter the SSH connection string (e.g., `ec2-user@<EC2_PUBLIC_IP>`).
   - Accept the host fingerprint if prompted.

### Step 3: Setup the Python Environment on EC2

1. **Update the EC2 Instance**:
   ```bash
   sudo apt-get update
   sudo apt-get upgrade -y
   ```

2. **Install Python**:
   ```bash
   sudo apt-get install python3-pip python3-dev -y
   sudo apt-get install python3-venv -y
   ```

3. **Clone the GitHub Repository**:
   ```bash
   git clone https://github.com/vanhoangkha/Technical-Analyst-Stock-Markets.git
   cd Technical-Analyst-Stock-Markets
   ```

4. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

5. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Step 4: Deploy and Run the Streamlit App

1. **Run the Streamlit App**:
   ```bash
   streamlit run Home.py --server.port 8080
   ```

2. **Access the App**:
   - Open a web browser and navigate to `http://<EC2_PUBLIC_IP>:8080`.
   - You should see the "Technical Analyst Stock Markets" app running.

### Step 5: Configuring EC2 for Production

1. **Running the App in Background**:
   To keep the app running after closing the SSH session, use `nohup`:
   ```bash
   nohup streamlit run Home.py --server.port 8080 &
   ```

2. **Security Best Practices**:
   - **Enable SSL**: Use a reverse proxy like Nginx to enable HTTPS.
   - **Monitoring**: Set up CloudWatch to monitor your EC2 instance's performance.
   - **Auto-Scaling**: Consider using Auto Scaling groups for handling increased traffic.

3. **Optimize Costs**:
   - Stop the EC2 instance when not in use to avoid unnecessary charges.
   - Consider using Spot Instances for cost savings.

### Conclusion

This guide demonstrated how to deploy the "Technical Analyst Stock Markets" Streamlit app on AWS EC2 using Visual Studio Code. By following these steps, you ensure that your application is production-ready, scalable, and secure. For more information on enhancing your application, consider integrating with additional AWS services like Amazon RDS for database management or Amazon S3 for storing static assets. 

Happy coding!