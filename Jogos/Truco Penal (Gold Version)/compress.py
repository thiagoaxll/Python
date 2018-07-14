# *********************************************************************************************
# ******   FATEC - Faculdade de Tecnologia de Carapicuiba                                ******
# ******   Funcao: responsavel por efetuar o processamento principal do jogo com todas   ******
# ******           as regras, definicoes e comportamento da aplicacao cliente            ******
# ******   Nome..: Diego Vinicius de Mello Munhoz                                        ******
# ******           Thiago Zacarias da Silva                                              ******
# ******           Victor Otavio Ponciano                                                ******
# ******   Data..: 07/07/2018                                                            ******
# *********************************************************************************************

from PIL import Image, ImageFile
from sys import exit, stderr
from os.path import getsize, isfile, isdir, join
from os import remove, rename, walk, stat
from stat import S_IWRITE
from shutil import move
# from argparse import ArgumentParserd
from abc import ABCMeta, abstractmethod

class ProcessBase:
    """Classe base abstrata para processamento dos arquivos."""
    __metaclass__ = ABCMeta

    def __init__(self):
        self.extensions = []
        self.backupextension = 'backup'

    @abstractmethod
    def processarArquivo(self, filename):
        """Metodo abstrato que realiza o processo no arquivo especificado.
           Retorna Verdadeiro se for bem-sucedido, Caso contrario, e falso."""
        pass

class ComprimirImagem(ProcessBase):
    """Processamento para reduzir o tamanho do arquivo de imagem."""

    def __init__(self):
        ProcessBase.__init__(self)
        self.extensions = ['jpg', 'jpeg', 'png']

    def processarArquivo(self, filename):
        """Renomeia a imagem especificada para um caminho de
           backup e gera uma nova imagem contendo com as configuracoes ideais."""
        try:
            # Ignorar arquivos somente leitura
            if (not stat(filename)[0] & S_IWRITE):
                print('Ignorando o arquivo somente-leitura"' + filename + '".')
                return False

            # Criando o backup
            backupname = filename + '.' + self.backupextension

            if isfile(backupname):
                print('Ignorando o arquivo "' + filename + '" para o qual o arquivo de backup ja existe.')
                return False

            rename(filename, backupname)
        except Exception as e:
            stderr.write('Ignorando o arquivo "' + filename + '" para o qual o backup nao pode ser feito - COD ERRO: ' + str(e) + '\n')
            return False

        ok = False

        try:
            # Abrindo a imagem
            with open(backupname, 'rb') as file:
                img = Image.open(file)

                # Verifique se e um formato suportado
                format = str(img.format)
                if format != 'PNG' and format != 'JPEG' and format != 'JPG':
                    print('Ignorando o arquivo "' + filename + '" com formato nao suportado ' + format)
                    return False

                # Esta linha evita problemas que podem surgir salvando arquivos JPEG maiores com PIL
                ImageFile.MAXBLOCK = img.size[0] * img.size[1]

                img.save(filename, quality=90, optimize=True)

            # Verifique se realmente comprimiu o arquivo
            origsize = getsize(backupname)
            newsize = getsize(filename)

            if newsize >= origsize:
                print('Nao foi possivel comprimir o arquivo "' + filename + '", arquivo ja esta reduzido.')
                return False

            # Sucesso na compressao
            ok = True
        except Exception as e:
            stderr.write('Falha durante o processamento "' + filename + '" - COD ERRO: ' + str(e) + '\n')
        finally:
            if not ok:
                try:
                    move(backupname, filename)
                except Exception as e:
                    stderr.write('ERROR: nao foi possivel restaurar o arquivo de backup para "' + filename + '": ' + str(e) + '\n')

        return ok

class DescomprimirImagem(ProcessBase):
    """Processamento que restaura a imagem do backup."""

    def __init__(self):
        ProcessBase.__init__(self)
        self.extensions = [self.backupextension]

    def processarArquivo(self, filename):
        """Move o arquivo de backup de volta ao seu nome original."""
        try:
            move(filename, filename[: -(len(self.backupextension) + 1)])
            return True
        except Exception as e:
            stderr.write('Falha ao restaurar o arquivo de backup"' + filename + '": ' + str(e) + '\n')
            return False