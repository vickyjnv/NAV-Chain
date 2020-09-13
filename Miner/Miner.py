import sys, os
sys.path.insert(0, os.path.abspath('..'))

from Model.Block import Block
from Model.BlockChain import BlockChain
from Model.User import User
from Utils.Ipfs import ipfs
import time
import random
import requests
class Miner:
	def __init__(self,id,lastblockAddress,genre,size):
		self.id=id
		self.blockChain=BlockChain(lastblockAddress)
		self.previous_hash=""
		self.genre=""
		self.size=""
		self.newsfiles=[]
		self.peerIp=[]
		self.clientIp=[]
		self.unverifiednews=[]
		self.vote={}
		self.creatorList={}
		self.castvote={}
		#download last block in blockchain
		userContent=self.blockChain.getUserContent()
		previousHash=self.blockchain.getBlockHash()
		self.block=Block(id,previousHash,lastblockAddress,genre,size,userContent)

	def ReceiveContent(self,miner_id,id,text,genre):
		#Code for recieving file from content creator
		# if not os.path.exists("NAV/NewsContent"):
		# 	os.mkdir("NAV/NewsContent")
		temp={"miner_id":miner_id,"id":id,"text":text,"genre":genre}
		self.unverifiednews.append({"miner_id":miner_id,"id":id,"text":text,"genre":genre})
		for x in self.peerIp:
			if(id==self.id):
				#should be done in async fashion
				requests.post("{}:80005/getNewsfromPeer".format(x), data = temp)
		#Get file from creators and store in this directory
		# self.creatorList[fileName]=creatorId
		return ""

	def ShowContent(self):
		return ""
		# if os.path.exists("NAV/NewsContent")
		# 	return os.listdir("NAV/NewsContent")

	def SelectNews(self,fileName):
		#Write code for selecting  news
		if fileName not in self.newsfiles:
			self.newsfiles.remove(fileName)

	def DeSelectNews(self,fileName):
		if fileName in self.newsfiles:
			self.newsfiles.remove(fileName)

	def sendBlockForVoting(self):
		block={
			"Miner":self.id,
			"Files":self.newsfiles
		}
		jsonBlockData=json.dumps(block)
		#Send this json file to all miners


	def recieveBlockForVoting(self):
		if not os.path.exists("NAV/NewsVotingContent"):
			os.mkdir("NAV/NewsVotingContent")
		#Store file in this directory in json format
		pass

	

	def doVoting(self):
		fileArray=os.listdir("NAV/NewsVotingContent")
		for file in fileArray:
			f=open(file,"r")
			data=json.load(f)
			miner=data["Miner"]
			newsfiles=data["Files"]
			self.block.updateVote(miner,newsfiles)
		self.block.calculateVotingScore()

	
	def requestConsensus(self):
		#Generate a random number between 1 and 100000
		minerFileHash=self.block["Body"]["UserContent"][self.id]
		minerRating=self.blockChain.getMiningRating(minerFileHash)
		age==self.blockChain.getMinerAge(minerFileHash)
		randomNumber=random.randrange(100000)
		data={
			"Miner":self.id,
			"MinerRating":minerRating,
			"BlockScore":self.block["Header"]["BlockScore"],
			"Age":age,
			"RandomNumber":randomNumber
		}
		#Send this data to all random number
	def RecieveConsensus(self):
		#Recieve json file and store it in a directory ConsensunDirectory
		directory="NAV/ConsensusDirectory"
		if not os.path.exists(directory):
			os.mkdir(directory)
		pass
	def consensusAlgorithm(self):
		#recieve the data and store in a directory in json form
		directory="NAV/ConsensusDirectory"
		fileArray=os.listdir(directory)
		totalRequest=0
		scorelist=[]
		randomNumber=[]
		for file in fileArray:
			totalRequest=totalRequest+1
			f=open(file,"r")
			data=json.load(f)
			miner=data["Miner"]
			score=data["MinerRating"]*(1-math.pow(math.e,-1*data["Age"]))
			minerList.append[miner]
			scorelist.append[score]
			randomNumber.append[data["RandomNumber"]]
		mean=randomNumber.mean()
		minerList=[x for _,x in sorted(zip(scoreList,minerList))]
		randomNumber=[x for _,x in sorted(zip(scoreList,randomNumber))]
		score.sort()
		start=int(totalRequest*0.75)
		end=totalRequest
		minDifference=float('inf')
		for i in range(start,end):
			diff=math.abs(randomNumber[i]-mean)
			if(diff<minDifference):
				finalMiner=minerList[i]
		if finalMiner.equals(self.id):
			self.BlockStatus=True	
		else:
			self.BlockStatus=False



	def CreateBlockForPublishing(self):
		#Write code for creating a block
		if not self.BlockStatus:
			return
		self.block=Block(self.id,self.previous_hash,self.previousHashBlockAddress,self.genre,self.size)
		newsFileHash=[]
		fileToHash={}
		for news in self.newsfiles:
			newsHash=ipfs.sendFile(news)
			newsFileHash.append(newsHash)
			creatorId=self.creatorList[news]
			fileToHash[news]=newsHash

		self.block.addNews(newsFileHash)
		self.block.createNewsMerkleTree(newsFileHash)

		
		#update ContentCreator Rating
		for creator,content in creatorList.keys():
			userFileHash=self.block["Body"]["UserContent"][creator]
			ipfs.downloadFile(userFileHash,"user.json")
			f=open("user.json","r")
			data=json.load(f)
			f.close()
			user=User(data["UserId"],data["VotingRating"],data["ContentRating"],data["ContentList"],data["MiningRating"],data["UpiId"],data["BlockList"],data["NavBirth"])
			#Calculate contentRating
			contentRating=self.block.calculateContentRating(creator)
			user.updateContentRating(contentRating)
			user.updateContentList(fileToHash[content])
			userFile=json.dumps(user.getUser(),indent=4)
			f=open("userFile.json","wb")
			f.write(userFile)
			f.close()
			UserId.append(creator)
			UserFileHash.append(ipfs.sendFile("user.json"))
		

			

		minerFileHash=self.block["Body"]["UserContent"][self.id]
		miningRating=self.block.CalculateMiningRating(miner)
		ipfs.downloadFile(minerFileHash,"miner.json")
		f=open("miner.json","r")
		data=json.load(f)
		f.close()
		user=User(data["UserId"],data["VotingRating"],data["ContentRating"],data["ContentList"],data["MiningRating"],data["UpiId"],data["BlockList"],data["NavBirth"])
		user.updateMiningRating(miningRating)
		userFile=json.dumps(user.getUser(),indent=4)
		f=open("userFile.json","wb")
		f.write(userFile)
		f.close()
		UserId.append(creator)
		UserFileHash.append(ipfs.sendFile("user.json"))
		self.block.update(UserId,UserFileHash)



	def publishBlock(self):
		blockFile=json.dumps(self.block.getBlock(),indent=4)
		blockFileName="block"+str(time.time())+".json"
		f=open(blockFileName,"wb")
		f.write(blockFile)
		f.close()
		blockAddress=ipfs.sendFile(blockFileName)

		#Send this blockaddress to all peers
		return blockAddress


	def resetMiningProcess(self):
		self.previous_hash=""
		self.genre=""
		self.size=""
		self.newsfiles=[]
		self.block=Block.Block(id,"","","",0,{})
