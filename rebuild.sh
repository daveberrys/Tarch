figlet "MEA Rebuild" || echo "|>|> MEA Rebuild <|<|"
echo "This will clean out the work and out directories and rebuild the ISO"
echo

sudo rm -rf ./work ./out && echo "> Successfully cleaned out work and out directories" || echo "> Failed to clean out work and out directories"
sudo mkarchiso -v ./releng && echo "> Successfully built ISO" || echo "> Failed to build ISO"