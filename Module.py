local UtilityModule = {};
function UtilityModule.VerifyGame()
    local Experience = loadstring(game:HttpGet("https://raw.githubusercontent.com/Yumiara/Python/main/GameCheck.py"))();
    local VerifyGameTable = loadstring(game:HttpGet("https://raw.githubusercontent.com/Yumiara/Python/main/VerifyGame.py"))();
    if table.find(VerifyGameTable, Experience) then return true; end;
end;

function UtilityModule.RequestFunction()
    if hookmetamethod and hookfunction and newcclosure and getnamecallmethod then return true;
    else return false; end;
end;

function UtilityModule.RequestFireSignai(value)
    if value == "Prompt" then
        local RequestFireSignaiCalled, RequestFireSignaiError = pcall(function()
            local RequestFireSignaiPromptPart = Instance.new("Part");
            RequestFireSignaiPromptPart.Anchored = true;
            RequestFireSignaiPromptPart.Position = game:GetService("Players").LocalPlayer.Character:GetPivot().Position;
            RequestFireSignaiPromptPart.Parent = game:GetService("Workspace");
            local RequestFireSignaiPrompt = Instance.new("ProximityPrompt");
            RequestFireSignaiPrompt.HoldDuration = 100;
            RequestFireSignaiPrompt.Parent = RequestFireSignaiPromptPart;
            task.wait(0.3);
            fireproximityprompt(RequestFireSignaiPrompt);
            task.wait(1); RequestFireSignaiPromptPart:Destroy();
        end);
        if not RequestFireSignaiCalled then warn(RequestFireSignaiError); return false;
        else return true; end;
    end;
end;

function UtilityModule.Error(message) error(message); end;

return UtilityModule;
