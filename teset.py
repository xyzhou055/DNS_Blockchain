import ast

List = "[{'left': 'b91516a9b918ed0e16f7dd2f0147d15b2628098fd91f533ae00450258d0504c4'}, {'right': 'c83a10b192f8da45522ab523d6651f6c794dd23b1259f9339b6bda4172254e20'}, {'right': 'b3ad54013f51d5bd1e7a7559ffb76924e4407afc94bf5a9db1fc5b9a92e6c6c6'}]"

print ast.literal_eval(List)
