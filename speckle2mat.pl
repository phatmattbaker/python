#!/usr/bin/env perl

open(DATA,"<ETH_particle.out") or die "Can't open data";
@lines = <DATA>;
close(DATA);

# check each row
$n = 0;
$line_count = 0;
	foreach my $line (@lines)
	{
		if($line =~ m/\%\%\sTrajectory/)
		{
			@start_traj[$n] = $linecount;
			$n++;
		}
		$linecount++;
	}

push(@start_traj,scalar @lines);
$number_of_traj =  scalar @start_traj;
print @start_traj,"\n";
print $start_traj[0];

# print @lines[(@start_traj[0] + 1)..(@start_traj[1]-1)];

for ($i=0;$i<$number_of_traj-1;$i++)
{
	$traj_no = $i+1;
	$file_title = "Trajectory_" . $traj_no . ".txt";
#	print $file_title;
	open (MYFILE, '>>', $file_title);
	print MYFILE @lines[(@start_traj[$i] + 1)..(@start_traj[$i+1]-1)];
	close MYFILE;
}

