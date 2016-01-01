function Update()
    local weatherData = ReadFileLines('C:\temp\weather.txt')
    
    Day1Meter = SKIN:GetMeter('meterDay1')
    Day1Meter:SetText(weatherData[0])   
   
end

function ReadFileLines(FilePath)
	-- HANDLE RELATIVE PATH OPTIONS.
	FilePath = SKIN:MakePathAbsolute(FilePath)

	-- OPEN FILE.
	local File = io.open(FilePath)

	-- HANDLE ERROR OPENING FILE.
	if not File then
		print('ReadFile: unable to open file at ' .. FilePath)
		return
	end

	-- READ FILE CONTENTS AND CLOSE.
	local Contents = {}
	for Line in File:lines() do
		table.insert(Contents, Line)
	end

	File:close()

	return Contents
end