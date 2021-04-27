[CmdletBinding()]
param
(
	[ValidateNotNullOrEmpty()]
	[String]
	$RepoRootPath,
	
	[ValidateNotNull()]
	[String[]]
	$Generators = @(),
	
	[ValidateNotNull()]
	[String[]]
	$Platforms = @(),
	
	[ValidateNotNull()]
	[String[]]
	$Integrations = @()
)

function TestGenerator
(
	[String]
	$RepoRootPath,

	[Hashtable]
	$TestCase,
	
	[String[]]
	$Platforms,
	
	[String[]]
	$Integrations
)
{	
	Write-Host "RootPath $($RepoRootPath)"

	$originalPath = (Get-Location).Path
	$generatorPath = Join-Path $RepoRootPath $TestCase.Path "generators\app"
	
	foreach ($scenario in $TestCase.scenarios)
	{
		if ($Platforms -and -not ($Platforms -contains $scenario.Platform))
		{
			Write-Warning "Generator: $($TestCase.Name) - Platform: $($scenario.Platform), Integration: $($scenario.Integration) | SKIPPED"
			continue
		}
		
		if ($Integrations -and -not ($Integrations -contains $scenario.Integration))
		{
			Write-Warning "Generator: $($TestCase.Name) - Platform: $($scenario.Platform), Integration: $($scenario.Integration) | SKIPPED"
			continue
		}
		
		try
		{
			$targetPath = Join-Path $TestCase.Name $scenario.Platform $scenario.Integration
			if (-not (Test-Path -Path $targetPath))
			{
				New-Item -ItemType Directory -Force -Path $targetPath 1> $null
			}
			
			$children = Get-ChildItem -Path $targetPath -Include *.* -File -Recurse
			foreach ($child in $children)
			{
				$child.Delete() 1> $null
			}
			
			Set-Location -Path $targetPath
			
			yo $generatorPath $TestCase.Name --platform $scenario.Platform --integration $scenario.Integration *> $null
			
			switch ($scenario.Platform)
			{
				"dotnet"
				{
					dotnet build 1> $null
					break
				}
				
				"js"
				{
					Set-Location -Path $TestCase.Name
					npm install 1> $null
					break
				}
			}
			
			Write-Information "Generator: $($TestCase.Name) - Platform: $($scenario.Platform), Integration: $($scenario.Integration) | SUCCESS"
		}
		catch
		{
			Write-Error "Generator: $($TestCase.Name) - Platform: $($scenario.Platform), Integration: $($scenario.Integration) | FAIL : $($_.Message)"
		}
		finally
		{
			Set-Location -Path $originalPath
		}
	}
}

$testCases = New-Object System.Collections.Generic.List[Object]

$testCases += @{
	Name = "Adaptive"
	Path = "generators\generator-bot-adaptive"
	Scenarios = @(
		@{
			Platform = "dotnet"
			Integration = "webapp"
		},
		@{
			Platform = "dotnet"
			Integration = "functions"
		},
		@{
			Platform = "js"
			Integration = "webapp"
		},
		@{
			Platform = "js"
			Integration = "functions"
		}
	)
}

$testCases += @{
	Name = "CoreAssistant"
	Path = "generators\generator-bot-core-assistant"
	Scenarios = @(
		@{
			Platform = "dotnet"
			Integration = "webapp"
		},
		@{
			Platform = "dotnet"
			Integration = "functions"
		}
	)
}

$testCases += @{
	Name = "CoreLanguage"
	Path = "generators\generator-bot-core-language"
	Scenarios = @(
		@{
			Platform = "dotnet"
			Integration = "webapp"
		},
		@{
			Platform = "dotnet"
			Integration = "functions"
		},
		@{
			Platform = "js"
			Integration = "webapp"
		},
		@{
			Platform = "js"
			Integration = "functions"
		}
	)
}

$testCases += @{
	Name = "CoreQnA"
	Path = "generators\generator-bot-core-qna"
	Scenarios = @(
		@{
			Platform = "dotnet"
			Integration = "webapp"
		},
		@{
			Platform = "dotnet"
			Integration = "functions"
		}
	)
}

$testCases += @{
	Name = "Empty"
	Path = "generators\generator-bot-empty"
	Scenarios = @(
		@{
			Platform = "dotnet"
			Integration = "webapp"
		},
		@{
			Platform = "dotnet"
			Integration = "functions"
		},
		@{
			Platform = "js"
			Integration = "webapp"
		},
		@{
			Platform = "js"
			Integration = "functions"
		}
	)
}

$testCases += @{
	Name = "EnterpriseAssistant"
	Path = "generators\generator-bot-enterprise-assistant"
	Scenarios = @(
		@{
			Platform = "dotnet"
			Integration = "webapp"
		},
		@{
			Platform = "dotnet"
			Integration = "functions"
		}
	)
}

$testCases += @{
	Name = "EnterpriseCalendar"
	Path = "generators\generator-bot-enterprise-calendar"
	Scenarios = @(
		@{
			Platform = "dotnet"
			Integration = "webapp"
		},
		@{
			Platform = "dotnet"
			Integration = "functions"
		}
	)
}

$testCases += @{
	Name = "EnterprisePeople"
	Path = "generators\generator-bot-enterprise-people"
	Scenarios = @(
		@{
			Platform = "dotnet"
			Integration = "webapp"
		},
		@{
			Platform = "dotnet"
			Integration = "functions"
		}
	)
}

foreach ($testCase in $testCases)
{
	if (-not $Generators -or ($Generators -contains $testCase.Name))
	{
		TestGenerator `
			-RepoRootPath $RepoRootPath `
			-TestCase $testCase `
			-Platforms $Platforms `
			-Integrations $Integrations
	}
	else
	{
		Write-Warning "Generator: $($testCase.Name) | SKIPPED"
	}
}
