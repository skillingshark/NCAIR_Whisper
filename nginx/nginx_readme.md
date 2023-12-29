# Readme file for serving through nginx ( to avoid shared array buffer problem )

## Step 01 : Setting Up nginx 
- Nginx works better on linux ( also more resources for nginx configurations are avalaible for linux )

- For setting up nginx on windows watch this video : https://www.youtube.com/watch?v=DKXdkXCgtCQ
  1. After the steps in the video you would have to modify the headers to enable shared array buffer so add these 2 add headers to the nginx.conf
     ```
          location / {
            root  "C:/nginx/ncair_whisper_deploy" ;
            index  index.html index.htm;
            add_header "Cross-Origin-Opener-Policy" "same-origin";   # Add this
            add_header "Cross-Origin-Embedder-Policy" "require-corp"; # Add this 
        }
     ```
